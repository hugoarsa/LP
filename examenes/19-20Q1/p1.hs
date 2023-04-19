main :: IO ()  
main = do 
    input <- getContents
    print (resultat input)

resultat :: String -> Int
resultat list = suma $ map (\x -> (read x)::Int) $ words list

suma :: [Int] -> Int
suma [] = 0
suma (x:xs) = x + suma xs