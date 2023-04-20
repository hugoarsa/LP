import Data.List (sort)

type Pos = (Int, Int)       -- la casella inferior esquerra és (1,1)

dins :: Pos -> Bool
dins (a,b) = 1<=a && a<=8 && 1<=b && b<=8

moviments :: Pos -> [Pos]
moviments (a,b) = filter dins $ zipWith sum_pos (take 8 $ repeat (a,b)) mov
    where 
        sum_pos (x,y) (z,w) = (x+z,y+w)
        mov = [(1,2),(2,1),(1,-2),(2,-1),(-1,2),(-2,1),(-1,-2),(-2,-1)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 (a,b) (c,d) = elem (c,d) $ concat $ map moviments $ concat $ map moviments $ moviments (a,b)

potAnar3' :: Pos -> Pos -> Bool
potAnar3' i q = elem q (((moviments i) >>= moviments) >>= moviments)