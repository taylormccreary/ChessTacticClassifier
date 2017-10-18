# Steps for scraping tactics from Chess.com
**Use beautifulsoup package**
1. Go to https://www.chess.com/tactics/problems?tagId=11 (different tagId for each type of tactic)
2. For each row, if rating < 1200 and moves = 1, add ID to array
	* Establish max rating
3. Do this for many pages, until the array is big enough. (https://www.chess.com/tactics/problems?tagId=11&page=2, increment page)
    * Define "big enough"
4. Iterate through the array, go to each URL and pull PGN
5. For each PGN, parse for {Chess.com id, FEN, solution move, label}