def distance1(x1, y1, x2, y2):
    # return the distance points (x1, y1) and (x2, y2)
    # Usage example: d1 = distance1 (0.0, 0, 3, 4) -> d1 = 5.0
    return (float(x1-x2)**2 + float(y1-y2)**2)**.5

def distance2(p1, p2):
    # p1 and p2 are lists
    # each list is a point, which has 2 indices, storing x and y
    # returns the distacne between p1 and p2
    # Usage example: d2 = distance2 ([0.0, 0], [3, 4]) -> d2 = 5.0
    return (float(p1[0]-p2[0])**2 + float(p1[1]-p2[1])**2)**.5

def distance3(c1, c2):
    # c1 and c2 are lists that represent circles
    # each list has 3 indices, storing center x and y, and radius
    # returns the distance between the center of c1  and c2, as well as
    # display if the circle c1 and c2 are overlapping or not
    # Usage example: d3, overlap = distance3([[0.0, 0, 1], [5, 0, 2]])
    # -> d3 = 5.0, overlap = False
    dist = distance2(c1, c2)
    return (dist, c1[2]+c2[2]>=dist)

def perimeter(points):
    # points is a list of points
    #       each point is a list with 2 indices (storing x and y)
    #       these points are the corners of the polygon (for k-gon,
    #       there are k points total, k>=3)
    # returns the perimeter of the polygon that is defined by the
    # input poitns
    sum = 0
    for i in range(len(points)):
        sum += distance2(points[i], points[i-1])
    return sum

exec(input().strip())