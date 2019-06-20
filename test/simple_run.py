import datetime
import visjs_timeline

groups = [visjs_timeline.TimeLineGroup("Group A", "A", 1),
          visjs_timeline.TimeLineGroup("Group B", "B", 2),
          visjs_timeline.TimeLineGroup("Group C", "C", 3),
          visjs_timeline.TimeLineGroup("Group D", "D", 4)]

items = [visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#1\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 1),
                                     "A",
                                     "red",
                                     "<div>1A tooltip</div>"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#2\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 2),
                                     "B",
                                     "blue",
                                     "2B tooltip"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#3\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 3),
                                     "C",
                                     "blue",
                                     "3C tooltip"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#4\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 4),
                                     "D",
                                     "green",
                                     "4D<br /> tooltip D2"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#5\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 5),
                                     "C",
                                     "yellow",
                                     "5C tooltip"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#6\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 6),
                                     "B",
                                     "violet",
                                     "6B tooltip"),
         visjs_timeline.TimeLineItem(visjs_timeline.ItemTitledContentRender.render("#7\nsubtitle", "detailed informations\n1\n2"),
                                     datetime.datetime(2019, 1, 1, 1, 1, 7),
                                     "A",
                                     "gray",
                                     "7A tooltip"),
         visjs_timeline.TimeLineItem("#8", datetime.datetime(2019, 1, 1, 1, 1, 8),
                                     "A",
                                     "gray",
                                     "8A tooltip"),

         ]

setting = visjs_timeline.TimeLineSetting(items, groups, "Test Page Title", visjs_timeline.themes.dark_time, "Test details")

# Auto create groups
# setting = visjs_timeline.TimeLineSetting(items, visjs_timeline.GroupsAutoBuilder.build(items), "Test Page Title", visjs_timeline.themes.dark_time, "Test details")


visjs_time_line = visjs_timeline.VisJsTimeLine()
visjs_time_line.render(setting)
visjs_time_line.save("test_output.html")