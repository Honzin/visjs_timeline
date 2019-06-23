import os
import copy
import datetime

from . import themes


class PackageDirectory:
    package_directory_path = os.path.abspath(os.path.dirname(__file__))

    @classmethod
    def resources(cls):
        return os.path.join(cls.package_directory_path, "resources")

    @classmethod
    def basic_template(cls):
        return os.path.join(cls.resources(), "basic_template.html")


class TimeLineSetting:
    def __init__(self, items, groups, page_title, theme, details=""):
        self.items = items
        self.groups = groups
        self.page_title = page_title
        self.theme = theme
        self.details = details


class ItemTitledContentRender:
    _template = "<div class=\"item_title\">%s</div>" \
                "<div class=\"item_detail\">%s</div>"

    @classmethod
    def render(cls, title, details):
        return cls._template % (cls._render_title(title), cls._render_details(details))

    @classmethod
    def _render_title(cls, title):
        return title.replace("\n", "<br />")

    @classmethod
    def _render_details(cls, details):
        result = ""
        for line in details.split("\n"):
            result += "<p>%s</p>" % line
        return result


class DetailsTableRender:
    _template = """
    <div class="left_block">
    <div class="details_table_title">%s</div>
    <table>
        %s
        
        %s
    </table>
    </div>
    """

    _header_column_template = "<th>%s</th>"
    _row_template = """
    <tr>
    %s
    </tr>
    """

    _column_template = "<td>%s</td>"

    @classmethod
    def render(cls, rows, title):
        cls._render_header(rows[0])

        return cls._template % (title, cls._render_header(rows[0]), cls._render_rows(rows[1:]))

    @classmethod
    def _render_header(cls, row):
        return cls._row_template % "\n".join([cls._header_column_template % column for column in row])

    @classmethod
    def _render_rows(cls, rows):
        result = ""
        for row in rows:
            result += cls._render_row(row)
        return result

    @classmethod
    def _render_row(cls, row):
        return "\n".join([cls._column_template % column for column in row])


class DetailTable:
    def __init__(self):
        self.rows = []
        self.title = ""


class DetailsTablesRender:
    _left_alignment_template = """
    <div class="left_block">
    %s
    </div>
    
    """

    _details_template = """
    
    <div class="details">
    %s
    </div>
    """

    @classmethod
    def render(cls, tables):
        result = ""
        for tables_in_row in tables:
            tmp_row = ""
            for table in tables_in_row:
                tmp_row += DetailsTableRender.render(table.rows, table.title)
            result += cls._details_template % tmp_row
        return result


class AutoId:
    _id = 0

    # TODO: reserved

    @staticmethod
    def generate():
        AutoId._id += 1
        return AutoId._id

    @staticmethod
    def reset():
        AutoId._id = 0


class TimeLineItem:
    def __init__(self, content, start, group_id, css_class_name, tooltip="", item_id=None):
        # TODO: It is not save. Add reserved list to AutoId
        self.item_id = item_id if item_id is not None else AutoId.generate()
        self.content = content
        self.start = start
        self.group_id = group_id
        self.css_class_name = css_class_name
        self.tooltip = tooltip
        # TODO: image


class TimeLineGroup:
    def __init__(self, content, group_id, value):
        self.content = content
        self.group_id = group_id
        self.value = value


class ItemRender:
    _template = "{id: %s," \
                " content: '%s'," \
                " start: new Date(%s, %s, %s, %s,%s,%s)," \
                " group: '%s'," \
                " className: '%s'," \
                " title: '%s'},\n"

    @classmethod
    def render(cls, item):
        return cls._template % (item.item_id,
                                item.content,
                                item.start.year,
                                item.start.month,
                                item.start.day,
                                item.start.hour,
                                item.start.minute,
                                item.start.second,
                                item.group_id,
                                item.css_class_name,
                                item.tooltip)


class GroupRender:
    _template = '{"content":  "%s", "id": "%s", "value": %s,},\n'

    @classmethod
    def render(cls, group):
        return cls._template % (group.content, group.group_id, group.value)


class GroupsAutoBuilder:
    @staticmethod
    def build(items):
        group_ids = set([item.group_id for item in items])
        return [TimeLineGroup(group_id, group_id, id) for group_id, id in zip(group_ids, enumerate(group_ids))]


class CssStyleRender:
    def __init__(self):
        self._css_styles = ""

    def render(self, style_names):
        self._css_styles = ""
        for style_name in style_names:
            css_style = self._read_style_file(style_name)
            self._css_styles += css_style
        return copy.copy(self._css_styles)

    def _read_style_file(self, style_name):
        with open(self._theme_path(style_name), "r") as theme_file:
            return theme_file.read()

    def _theme_path(self, style_name):
        return os.path.join(PackageDirectory.resources(), "%s.css" % style_name)


class VisJsTimeLine:
    style_including_mark = "INCLUDE_STYLE"
    groups_including_mark = "INCLUDE_GROUPS"
    items_including_mark = "INCLUDE_ITEMS"
    title_including_mark = "INCLUDED_TITLE"
    details_including_mark = "INCLUDED_DETAILS"

    def __init__(self):
        self.template_path = PackageDirectory.basic_template()
        self.rendered_html_content = ""
        self._setting = None

    def render(self, setting):
        self._setting = setting
        self._read_template()
        self._render_css_style()
        self._render_page_title()
        self._render_details()
        self._render_groups()
        self._render_items()

    def _read_template(self):
        with open(self.template_path, "r") as template_file:
            self.rendered_html_content = template_file.read()

    def _render_css_style(self):
        style_render = CssStyleRender()
        self.rendered_html_content = self.rendered_html_content.replace(self.style_including_mark, style_render.render(self._setting.theme))

    def _render_groups(self):
        rendered_groups = ""
        for group in self._setting.groups:
            rendered_groups += GroupRender.render(group)
        self.rendered_html_content = self.rendered_html_content.replace(self.groups_including_mark, rendered_groups)

    def _render_items(self):
        rendered_items = ""
        for item in self._setting.items:
            rendered_items += ItemRender.render(item)
        self.rendered_html_content = self.rendered_html_content.replace(self.items_including_mark, rendered_items)

    def _render_page_title(self):
        self.rendered_html_content = self.rendered_html_content.replace(self.title_including_mark, self._setting.page_title)

    def _render_details(self):
        self.rendered_html_content = self.rendered_html_content.replace(self.details_including_mark, self._setting.details)

    def save(self, output_file):
        with open(output_file, "w+") as output_file:
            output_file.write(self.rendered_html_content)



