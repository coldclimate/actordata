import urllib2
import simplejson
import os

# https://www.themoviedb.org/documentation/api
# and export it in your environment as "themoviedbkey"

apikey = os.environ['themoviedbkey']

actors = ["Gillian Anderson", "David Duchovny", "James McAvoy", "Forest Whitaker"]
#actors = ["Gillian Anderson"]
arrOutput = []

colors = ["aliceblue", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "chocolate", "coral", "cornflowerblue", "cornsilk", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dodgerblue", "firebrick", "forestgreen", "fuchsia", "gainsboro", "gold", "goldenrod", "gray", "green", "greenyellow", "honeydew", "hotpink", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgreen", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "pink", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "yellow", "yellowgreen"]

for actor in actors:
    objPerson = {
        "name": actor,
        "type": actor.replace(" ", "-").lower(),
        "films": [],
        "colour" : colors.pop()
    }
    print("Working in %s" % actor)
    opener = urllib2.build_opener()
    f = opener.open(urllib2.Request("https://api.themoviedb.org/3/search/person?query=%s&api_key=%s" % (actor.replace(" ", "%20"), apikey)))
    results = simplejson.load(f)
    id = results["results"][0]["id"]
    f.close

    if id:
        opener2 = urllib2.build_opener()
        f2 = opener.open(urllib2.Request("http://api.themoviedb.org/3/person/%s/credits?api_key=%s" % (id, apikey)))
        results2 = simplejson.load(f2)
        for role in results2["cast"]:
            objPerson["films"].append(role["title"]);

    arrOutput.append(objPerson)

print arrOutput

