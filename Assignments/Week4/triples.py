if __name__ == "__main__":
    triples = [(x,y,z) for x in range(1,4) for y in range(2,5) for z in range(5,8) if x+y>z]
    print(triples)

    pairs = [ (x,y) for x in range(3,0,-1) for y in range(2,0,-1) if (x+y)%3 == 0 ]
    print(pairs)

    pairs2 = [ (x,y) for x in range(5,1,-1) for y in range(4,1,-1) if (x+y)%3 == 0 ]
    print(pairs2)