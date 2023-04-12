myUnfoldr :: (b -> Maybe (a, b)) -> (b -> [a])
myUnfoldr f b = case f b of
                Just (a, b') -> a : myUnfoldr f b'
                Nothing -> []

myReplicate :: a -> Int -> [a]
myReplicate a b = myUnfoldr (\x -> if x == 0 then Nothing else Just (a, x - 1)) b

myIterate :: (a -> a) -> a -> [a] 
myIterate f a = myUnfoldr (\x -> Just(x, f x)) a

myMap :: (a -> b) -> [a] -> [b]
myMap f xs = myUnfoldr (\x -> if null x then Nothing else Just(f (head x),tail x)) xs

data Bst a = Empty | Node a (Bst a) (Bst a)
 
add :: Ord a => a -> (Bst a) -> (Bst a)
add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y          = Node y (add x l) r
    | x > y          = Node y l (add x r)
    | otherwise = Node y l r

instance Show a => Show (Bst a) where
    show Empty = "."
    show (Node root l r) = "(" ++ show root ++ " " ++ show l ++ " " ++ show r ++ ")"


adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
adder (t, []) = Nothing
adder (t, (x:xs)) = Just (new, (new, xs))
    where 
        new = add x t