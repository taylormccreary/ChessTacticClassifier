
# Chess Tactic Classifier
A program that classifies chess tactics based on the concepts they demonstrate.

## Table of Contents
- Abstract
- Timeline
- Data sources
- Technologies
- Club resources
- End Goal

## Abstract
To improve their skills, many chess players practice simple chess puzzles of one or two moves. These puzzles can be grouped based on the different concepts or strategies they illustrate, and learning and recognizing these patterns is a key skill for competitive chess players. We are going to build a program that recognizes three types of tactics: forks, skewers and trapped pieces.

<table>
 <tr>
  <td>
   <h3>Trapped Piece</h3>
   <img src="trapped_piece_example.png" align="middle">
  </td>
  <td>
   <h3>Fork</h3>
   <img src="fork_example.png" align="middle"> 
  </td>
  <td>
   <h3>Skewer</h3>
   <img src="skewer_example.png" align="middle">
  </td>
 </tr>
 </table>
 
## Timeline
### Week 3
- Verify data source, web scraping, have data
- fork.csv
- FEN, Qe3, d4, white
- FEN, b6, Be4, black

### Week 4
- Clean data, data features

### Week 5
- Clean data, design models

### Week 6
- Design models, UI design

### Week 7
- Design models, UI design

### Week 8
- Polishing project

### Week 9
- Buffer week

## Data sources
- Chess.com

## Technologies
- python for scraping data
- python for machine learning
- python (django) / js for webapp building

## Club resources required
- guidance on web scraping and building the webapp

## End Goal
A webapp that users can copy and paste a chess position (in the form of an FEN string) and see the position displayed, with the category of tactic the program outputs. 
