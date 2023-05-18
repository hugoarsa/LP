data Tree a = Empty | Node a (Tree a) (Tree a)
    deriving (Show)

instance Foldable (Tree) where
    foldr f x0 Empty = x0
    foldr f x0 (Node x1 l r) = f x1 (foldr f (foldr f x0 r) l)

avg :: Tree Int -> Double
avg arbre = (fromIntegral $ sum arbre) / (fromIntegral $ length arbre) 

cat :: Tree String -> String
cat = foldr f ""
    where
        f a b 
         | a == "" = b 
         | otherwise = a ++ " " ++ b
