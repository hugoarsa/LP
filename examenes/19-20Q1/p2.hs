degree :: Eq a => [(a, a)] -> a -> Int
degree [] v = 0
degree ((x,y):xs) v
    | x == v || y == v = 1 + (degree xs v)
    | otherwise        = degree xs v
    where
        next = degree xs v

degree' :: Eq a => [(a, a)] -> a -> Int
degree' xs v = foldl deg_f 0 xs 
    where
        deg_f acc (x,y)
            | x == v || y == v = 1 + acc
            | otherwise        = acc
