import json

from osgeo import ogr
from osgeo import osr

source = osr.SpatialReference()
source.ImportFromEPSG(4326)

target = osr.SpatialReference()
target.ImportFromEPSG(5243)

transform = osr.CoordinateTransformation(source, target)
transformBack = osr.CoordinateTransformation(target, source)

with open('kenyapop/popdata_geojson.json') as f:
    gj = json.loads(f.read())

features = gj['features']
output = []

def area(coordList):
    s = 0.0
    for i in range(0, len(coordList) - 1):
        s += (coordList[i][0]*coordList[i+1][1]) - (coordList[i+1][0]*coordList[i][1])
    
    return 0.5 * s

def centroid(coordList, a):
    c = [0.0, 0.0]

    for i in range(0, len(coordList) - 1):
        c[0] += (coordList[i][0] + coordList[i+1][0]) * (coordList[i][0]*coordList[i+1][1] - coordList[i+1][0]*coordList[i][1])
        c[1] += (coordList[i][1] + coordList[i+1][1]) * (coordList[i][0]*coordList[i+1][1] - coordList[i+1][0]*coordList[i][1])

    c[0] = c[0] // (a*6)
    c[1] = c[1] // (a*6)

    return c

for feature in features:
    coords = feature['geometry']['coordinates'][0]
    poly = ogr.CreateGeometryFromJson(str(feature['geometry']))
    poly.Transform(transform)
    a = poly.GetArea()
    # a = area(coords)
    # the following doesn't work
    # c = poly.Centroid()
    # c.Transform(transformBack)
    minLat = 180
    maxLat = -180
    minLong = 180
    maxLong = -180

    for point in coords:
        if point[0] < minLat:
            minLat = point[0]
        if point[0] > maxLat:
            maxLat = point[0]
        
        if point[1] < minLong:
            minLong = point[1]
        if point[1] > maxLong:
            maxLong = point[1]
    
    c = [(minLat + maxLat) / 2, (minLong + maxLong) / 2]

    # geojson is backwards?? longlat??
    output.append([c[1], c[0], a])

f = open("kenyapop/heatmap_pointdata.json", "w")
f.write(json.dumps(output))
f.close()

