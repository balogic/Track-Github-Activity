import feedparser
print "Enter the Github username to track:"
uname = raw_input()
a = feedparser.parse("http://github.com/%s.atom"%uname)
for activity in a.entries:
	print activity.title


