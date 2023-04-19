data Tree a = Empty | Node a (Tree a) (Tree a)

data Forest a = [] | a : (Forest a)

instance Show a => Show (Tree a) where
    show Empty = "()"
    show (Node root l r) = "(" ++ show l ++ "," ++ show root ++ "," ++ show r ++ ")"

instance Functor Tree where
    fmap f Empty = Empty
    fmap f (Node x fe fd) = Node (f x) (fmap f fe) (fmap f fd)

instance Functor Forest where
    fmap f (x:xs) = ((f x):(fmap xs))

doubleT :: Num a => Tree a -> Tree a
doubleT a = fmap (*2) a

doubleF :: Num a => Forest a -> Forest a 
doubleF a = fmap doubleT a