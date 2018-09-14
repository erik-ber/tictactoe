

import Wrapper
import Cards
import Test.QuickCheck hiding (shuffle)
import Data.Char
import Data.List


deleteN :: Int -> [a] -> [a]
deleteN _ []     = []
deleteN i (a:as)
    | i == 0    = as
    | otherwise = a : deleteN (i-1) as

aCard1 :: Card
aCard1 = Card (Numeric 7) Hearts

aCard2 :: Card
aCard2 = Card Ace Clubs

aCard3 :: Card
aCard3 = Card Ace Hearts

aHand :: Hand
aHand = [aCard1, aCard2]

aHand2 :: Hand
aHand2 = [aCard3, aCard2]

--Task B
{-Note that I'm using a lambda function in the map function to avoid writing another function that would
be called showCard-}
display :: Hand -> String
display hand = intercalate ", " (map (\n -> show (rank n) ++ " of " ++ show (suit n)) hand)
--Task C
valueRank::Rank -> Int
valueRank Ace         = 11
valueRank (Numeric n) = n 
valueRank _           =  10

value :: Hand -> Int
value hand = sum(map valueRank (map rank hand))

--Task D
gameOver :: Hand -> Bool
gameOver hand | value hand > 21 = True | otherwise = False

winner :: Hand -> Hand -> Player
winner hand1 hand2 | gameOver hand1 = Bank | gameOver hand2 = Guest | value hand1 > value hand2 = Guest 
    | otherwise = Bank
--Task E
ranks = [(Numeric 2), (Numeric 3), (Numeric 4), (Numeric 5), (Numeric 6)
    , (Numeric 7), (Numeric 8), (Numeric 9), (Numeric 10), Jack, Queen, King, Ace]

createCard :: Suit -> Rank -> Card
createCard suit rank = Card rank suit

generateDeckForSuit :: Suit -> [Card] 
generateDeckForSuit suit = map (createCard suit) ranks

fullDeck :: Deck
fullDeck = generateDeckForSuit Hearts ++ generateDeckForSuit Spades
     ++ generateDeckForSuit Clubs ++ generateDeckForSuit Diamonds

prop_size_fullDeck :: Bool
prop_size_fullDeck = size (fullDeck) == 52
--Task F
draw :: Deck -> Hand -> (Deck, Hand)
draw deck hand | size(deck) == 0 = error "draw: The deck is empty."|
     otherwise = (deleteN 0 (deck), ((deck !! 0) : hand))
--Task G
--playBank :: Deck -> Hand
playBank' deck bankHand | value bankHand >= 16 = bankHand
                        | otherwise = playBank' deck' bankHand' where (deck', bankHand') = draw deck bankHand
--Task H
