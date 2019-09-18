# -*- coding: utf-8 -*-

'''
https://leetcode.com/discuss/interview-question/375258/Twitter-or-OA-2019-or-Game-Events
'''
import re
class Solution(object):
	def splitEvent(self, team, events):
		event_priority = ['G', 'Y', 'R', 'S']

		ans = []
		for event in events:
			split_event = event.split(" ")
			time, extra_time = '', '0'
			time_idx = 0
			for i, e in enumerate( split_event ):
				if re.match("^[0-9+]*$", e):
					time_idx = i
					if e.isdigit():
						time = e
					else:
						e = e.split("+")
						time, extra_time = e[0], e[1]
					break
			player = " ".join( split_event[:time_idx] )
			event_idx = event_priority.index( split_event[ time_idx + 1 ] )

			if event_idx == 3:
				second_player = " ".join( split_event[time_idx+2:] )
			else:
				second_player = ""

			new_event = [ time, extra_time, event_idx, team, player, second_player, team + " " + event ]
			ans.append( new_event )

		return ans

	def getEventsOrder(self, team1, team2, events1, events2):
		listEvents = []
		listEvents += self.splitEvent( team1, events1 )
		listEvents += self.splitEvent( team2, events2 )

		listEvents.sort( key=lambda x: (x[0], x[1], x[2], x[3], x[4], x[5]) )

		ans = [ x[6] for x in listEvents ]

		return ans

		




s = Solution()
print s.getEventsOrder('EDC', 'CDE', ['Name1 12 G','FirstName LastName 43 Y'], ['Name3 45+1 S SubName','Name4 46 G'])