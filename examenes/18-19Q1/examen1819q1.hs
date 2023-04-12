getNumber :: Char -> Int
getNumber x
    | x == 'I'  = 1
    | x == 'V'  = 5
    | x == 'X'  = 10
    | x == 'L'  = 50
    | x == 'C'  = 100
    | x == 'D'  = 500
    | otherwise = 1000

roman2int :: String -> Int
roman2int [] = 0
roman2int [x] = getNumber x
roman2int (x:y:xs)
    | n < m     = roman2int (y:xs) - n
    | otherwise = roman2int (y:xs) + n
        where
            n = getNumber x
            m = getNumber y

roman2int' :: String -> Int
roman2int' roman = nums2int' $ map getNumber roman
    where
        nums2int' :: [Int] -> Int
        nums2int' nums = sum $ zipWith sumOrSubs (nums) (tail nums ++ [0])
            where
                sumOrSubs :: Int -> Int -> Int
                sumOrSubs x next
                    | x >= next = x
                    | otherwise = -x

arrels :: Float -> [Float] 
arrels x = (x:(sub_arrel x))
    where
        orig = x
        sub_arrel :: Float -> [Float]
        sub_arrel prev = (next:(sub_arrel next))
            where next = 0.5 * (prev + (orig / prev))

arrel :: Float -> Float -> Float
arrel x e = arrel' (arrels x) e
    where
        xs = arrels x
        arrel' :: [Float] -> Float -> Float
        arrel' (x1:x2:xs) e
            | abs(x2 - x1) < e  = x2
            | otherwise         = arrel' (x2:xs) e

data LTree a = Leaf a | Node (LTree a) (LTree a)

instance Show a => Show (LTree a) where
    show (Leaf a) = "{" ++ show a ++ "}"
    show (Node l r) = "<" ++ show l ++ "," ++ show r ++ ">"

build :: [a] -> LTree a
build xs = build' $ map Leaf xs
    where
        build' :: [LTree a] -> LTree a
        build' [x] = x
        build' xs = Node (build' (take n xs)) (build' (drop n xs))
            where
                n = div (length xs + 1) 2

zipLTrees :: LTree a -> LTree b -> Maybe (LTree (a,b))
zipLTrees (Leaf a) (Leaf b) = Just $ Leaf (a,b)
zipLTrees (Leaf a) _ = Nothing
zipLTrees _ (Leaf b) = Nothing
zipLTrees (Node l1 r1) (Node l2 r2) = do
    l <- zipLTrees l1 l2
    r <- zipLTrees r1 r2
    return $ Node l r
