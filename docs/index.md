---
title: "Deadliest Chess Opening Traps"
layout: post
---

### An analysis of online games played by real, fallible humans

For computers and top-level players, chess is a game of precision and cumulation of small advantages. Yet for the rest of us humans, certain opening positions can lead to large advantages, particularly in games with short time controls. 

I sought to identify the deadliest chess openings by analyzing online games through the wonderful Lichess database API. My search strategy involved two main "deadliness" critera: the final position should have a high proportion of wins for a given attacking side, and the sequence of moves by the defending side must be likely to occur (e.g. among the most common moves played). Below are the top 50 openings that arose from this analysis, ranked by win proportion by White. 

#### Trap #1, Modern Defense

1\. d4 g6 2. e4 Bg7 3. Bh6 d6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/eOatZRN4/white#6">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_1.svg" alt="Chess Board for Trap #1" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_1.svg" alt="Win-Loss plot for Trap #1" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 19.3%
<br>
Probability of opponent playing into this position (including first move): 1.0%
<br>
Stockfish evaluation: +11.5. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/eOatZRN4/white#6">https://lichess.org/eOatZRN4/white#6</a>
<br>
Comment: A speed chess trick hoping to capture the bishop on g7. White hopes that Black has premoved the next move such as 3...d6 shown here



#### Trap #2, Horwitz Defense

1\. d4 e6 2. Bg5 d5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/leVXRiTr/white#4">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_2.svg" alt="Chess Board for Trap #2" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_2.svg" alt="Win-Loss plot for Trap #2" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 30.3%
<br>
Probability of opponent playing into this position (including first move): 3.0%
<br>
Stockfish evaluation: +9.6. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/leVXRiTr/white#4">https://lichess.org/leVXRiTr/white#4</a>
<br>
Comment: Another speed chess trick hoping for an early queen capture. In bullet time controls, 2...d5 is the most popular move, occurring in over 33% of games



#### Trap #3, Caro-Kann Defense: Breyer Variation

1\. e4 c6 2. d3 d5 3. Nf3 dxe4 4. Ng5 exd3 5. Bxd3 Nf6 6. Nxf7 Kxf7
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Ur37Kja3/white#12">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_3.svg" alt="Chess Board for Trap #3" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_3.svg" alt="Win-Loss plot for Trap #3" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 14.8%
<br>
Probability of opponent playing into this position (including first move): 1.2%
<br>
Stockfish evaluation: +5.3. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Ur37Kja3/white#12">https://lichess.org/Ur37Kja3/white#12</a>
<br>
Comment: A deadly tactical trap. On move 5, the most popular move played by Black is the natural-looking 5...Nf6, allowing the objectively sound 6.Nxf7. After the most popular 6...Kxf7 (shown), White wins the queen with the discovered attack 7.Bg6+



#### Trap #4, Zukertort Opening: Tennison Gambit

1\. Nf3 d5 2. e4 dxe4 3. Ne5 Nf6 4. Qh5 g6 5. Bc4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/gvdmtOgk/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_4.svg" alt="Chess Board for Trap #4" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_4.svg" alt="Win-Loss plot for Trap #4" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 11.8%
<br>
Probability of opponent playing into this position (including first move): 3.3%
<br>
Stockfish evaluation: -2.0. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/gvdmtOgk/white#9">https://lichess.org/gvdmtOgk/white#9</a>
<br>
Comment: An early checkmate trap. White tempts Black with the possibility of 5...gxh5, which gives checkmate in one with 6.Bxf7#. Black can defend with 5...e6, only slightly more frequently played in online games than the blunder



#### Trap #5, Caro-Kann Defense

1\. e4 c6 2. d4 d5 3. Nc3 dxe4 4. d5 cxd5 5. Qxd5 Qxd5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/xCPtvRVD/white#10">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_5.svg" alt="Chess Board for Trap #5" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_5.svg" alt="Win-Loss plot for Trap #5" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 26.5%
<br>
Probability of opponent playing into this position (including first move): 2.2%
<br>
Stockfish evaluation: +0.6. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/xCPtvRVD/white#10">https://lichess.org/xCPtvRVD/white#10</a>
<br>
Comment: While Stockfish gives White only a slight theoretical advantage, the tactical threats give White a whopping 73.1% win rate in online games



#### Trap #6, French Defense: Diemer-Duhm Gambit Accepted

1\. e4 e6 2. d4 d5 3. c4 dxe4 4. d5 exd5 5. cxd5 Nf6 6. Nc3 Bb4 7. Qa4+
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/n4DEbW0Q/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_6.svg" alt="Chess Board for Trap #6" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_6.svg" alt="Win-Loss plot for Trap #6" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 15.0%
<br>
Probability of opponent playing into this position (including first move): 1.8%
<br>
Stockfish evaluation: +4.8. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/n4DEbW0Q/white#13">https://lichess.org/n4DEbW0Q/white#13</a>
<br>
Comment: With a sequence of reasonable-looking moves, the move 6...Bb4 occurs in 55.6% of online games, losing either a bishop or a knight



#### Trap #7, Caro-Kann Defense

1\. e4 c6 2. Nc3 d5 3. Qe2 dxe4 4. Nxe4 Nf6 5. Nxf6+ gxf6 6. b3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/XHM2f2Nw/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_7.svg" alt="Chess Board for Trap #7" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_7.svg" alt="Win-Loss plot for Trap #7" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 20.4%
<br>
Probability of opponent playing into this position (including first move): 1.7%
<br>
Stockfish evaluation: -0.0. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/XHM2f2Nw/white#11">https://lichess.org/XHM2f2Nw/white#11</a>
<br>
Comment: Despite a relatively even computer evaluation, White gains an aggressive position and wins 71.9% of the time in online games



#### Trap #8, Scotch Game

1\. e4 e5 2. Nf3 Nc6 3. d4 exd4 4. Ng5 h6 5. Nxf7 Kxf7 6. Bc4+
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/26k0fiuA/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_8.svg" alt="Chess Board for Trap #8" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_8.svg" alt="Win-Loss plot for Trap #8" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 18.3%
<br>
Probability of opponent playing into this position (including first move): 5.8%
<br>
Stockfish evaluation: -3.9. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/26k0fiuA/white#11">https://lichess.org/26k0fiuA/white#11</a>
<br>
Comment: A deadly checkmate trap. In 51.3% of online games, Black continues with 6...Ke8, allowing 7.Qh5+ with forced checkmate to follow



#### Trap #9, Blackmar-Diemer Gambit

1\. d4 d5 2. e4 dxe4 3. Nc3 Nf6 4. Qe2 Bf5 5. Qb5+
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/dKSX3sqs/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_9.svg" alt="Chess Board for Trap #9" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_9.svg" alt="Win-Loss plot for Trap #9" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 16.2%
<br>
Probability of opponent playing into this position (including first move): 5.8%
<br>
Stockfish evaluation: -1.4. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/dKSX3sqs/white#9">https://lichess.org/dKSX3sqs/white#9</a>
<br>
Comment: A tricky position for Black to defend, with the most common continuation 5...Bd7 6.Qxb7 baiting Black into the blunder 6...Bc6, which wins at least a piece after 7.Bb5



#### Trap #10, Caro-Kann Defense: Advance Variation, Bayonet Attack

1\. e4 c6 2. d4 d5 3. e5 Bf5 4. g4 Bg6 5. h4 h6 6. h5 Bh7 7. e6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6NQJYD43/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_10.svg" alt="Chess Board for Trap #10" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_10.svg" alt="Win-Loss plot for Trap #10" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.3%
<br>
Probability of opponent playing into this position (including first move): 1.0%
<br>
Stockfish evaluation: +1.7. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6NQJYD43/white#13">https://lichess.org/6NQJYD43/white#13</a>
<br>
Comment: While there is no immediate tactical threat, this kingside pawn storm is theoretically sound with a favorable Stockfish evaluation and has a >70% win rate in online games



#### Trap #11, Nimzo-Larsen Attack

1\. b3 e6 2. Bb2 d5 3. Bxg7 Nf6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MbGzGHXW/white#6">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_11.svg" alt="Chess Board for Trap #11" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_11.svg" alt="Win-Loss plot for Trap #11" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 13.8%
<br>
Probability of opponent playing into this position (including first move): 1.3%
<br>
Stockfish evaluation: +7.2. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MbGzGHXW/white#6">https://lichess.org/MbGzGHXW/white#6</a>



#### Trap #12, Caro-Kann Defense: Exchange Variation

1\. e4 c6 2. d4 d5 3. exd5 cxd5 4. Bf4 Nc6 5. Nc3 Nf6 6. Nb5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/CEqgiBUC/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_12.svg" alt="Chess Board for Trap #12" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_12.svg" alt="Win-Loss plot for Trap #12" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 22.8%
<br>
Probability of opponent playing into this position (including first move): 1.9%
<br>
Stockfish evaluation: +1.5. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/CEqgiBUC/white#11">https://lichess.org/CEqgiBUC/white#11</a>



#### Trap #13, Bird Opening: From's Gambit, Lasker Variation

1\. f4 e5 2. fxe5 d6 3. exd6 Bxd6 4. Nf3 g5 5. d3 g4 6. Nd4 Qh4+ 7. g3 Bxg3+ 8. hxg3 Qxh1 9. Bf4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/PAmkoWnm/white#17">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_13.svg" alt="Chess Board for Trap #13" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_13.svg" alt="Win-Loss plot for Trap #13" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 23.3%
<br>
Probability of opponent playing into this position (including first move): 2.6%
<br>
Stockfish evaluation: +1.0. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/PAmkoWnm/white#17">https://lichess.org/PAmkoWnm/white#17</a>



#### Trap #14, Zukertort Opening: Tennison Gambit

1\. e4 d5 2. Nf3 dxe4 3. Ng5 Nf6 4. Qe2 Bf5 5. Qb5+
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Pvj11OSt/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_14.svg" alt="Chess Board for Trap #14" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_14.svg" alt="Win-Loss plot for Trap #14" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 16.1%
<br>
Probability of opponent playing into this position (including first move): 1.6%
<br>
Stockfish evaluation: -1.5. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Pvj11OSt/white#9">https://lichess.org/Pvj11OSt/white#9</a>



#### Trap #15, Sicilian Defense: Mengarini Variation

1\. e4 c5 2. a3 Nc6 3. b4 cxb4 4. axb4 Nxb4 5. d4 d5 6. c3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/oRF8G485/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_15.svg" alt="Chess Board for Trap #15" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_15.svg" alt="Win-Loss plot for Trap #15" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.1%
<br>
Probability of opponent playing into this position (including first move): 2.4%
<br>
Stockfish evaluation: 0.0. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/oRF8G485/white#11">https://lichess.org/oRF8G485/white#11</a>



#### Trap #16, Zukertort Opening: Tennison Gambit

1\. e4 d5 2. Nf3 dxe4 3. Ng5 Nf6 4. Nc3 Bf5 5. Bc4 e6 6. d3 exd3 7. Qf3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/IK6ea6vm/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_16.svg" alt="Chess Board for Trap #16" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_16.svg" alt="Win-Loss plot for Trap #16" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 15.1%
<br>
Probability of opponent playing into this position (including first move): 1.5%
<br>
Stockfish evaluation: -3.0. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/IK6ea6vm/white#13">https://lichess.org/IK6ea6vm/white#13</a>



#### Trap #17, Van Geet Opening: Dunst-Perrenet Gambit

1\. d3 d5 2. e4 dxe4 3. Nc3 exd3 4. Bg5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/fxU3bO2a/white#7">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_17.svg" alt="Chess Board for Trap #17" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_17.svg" alt="Win-Loss plot for Trap #17" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 54.5%
<br>
Probability of opponent playing into this position (including first move): 15.1%
<br>
Stockfish evaluation: -1.6. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/fxU3bO2a/white#7">https://lichess.org/fxU3bO2a/white#7</a>



#### Trap #18, Zukertort Opening: Tennison Gambit

1\. Nf3 d5 2. e4 dxe4 3. Ne5 Nf6 4. Bb5+ c6 5. Qh5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MkFiBN7u/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_18.svg" alt="Chess Board for Trap #18" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_18.svg" alt="Win-Loss plot for Trap #18" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 32.9%
<br>
Probability of opponent playing into this position (including first move): 9.2%
<br>
Stockfish evaluation: -14.1. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MkFiBN7u/white#9">https://lichess.org/MkFiBN7u/white#9</a>



#### Trap #19, Scandinavian Defense

1\. e4 d5 2. e5 d4 3. Bb5+ c6 4. Be2
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/pqAIdyFw/white#7">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_19.svg" alt="Chess Board for Trap #19" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_19.svg" alt="Win-Loss plot for Trap #19" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.5%
<br>
Probability of opponent playing into this position (including first move): 1.2%
<br>
Stockfish evaluation: -0.0. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/pqAIdyFw/white#7">https://lichess.org/pqAIdyFw/white#7</a>



#### Trap #20, English Opening: Anglo-Indian Defense

1\. c4 Nf6 2. g3 g6 3. Bg2 Bg7 4. Bxb7 O-O
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/SWoutFbJ/white#8">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_20.svg" alt="Chess Board for Trap #20" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_20.svg" alt="Win-Loss plot for Trap #20" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 19.8%
<br>
Probability of opponent playing into this position (including first move): 4.0%
<br>
Stockfish evaluation: +5.6. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/SWoutFbJ/white#8">https://lichess.org/SWoutFbJ/white#8</a>



#### Trap #21, Sicilian Defense: Wing Gambit, Abrahams Variation

1\. e4 c5 2. b4 cxb4 3. Bb2 Nc6 4. d4 d5 5. exd5 Qxd5 6. c4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MlqMgmlm/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_21.svg" alt="Chess Board for Trap #21" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_21.svg" alt="Win-Loss plot for Trap #21" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.6%
<br>
Probability of opponent playing into this position (including first move): 2.5%
<br>
Stockfish evaluation: +0.1. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/MlqMgmlm/white#11">https://lichess.org/MlqMgmlm/white#11</a>



#### Trap #22, Caro-Kann Defense

1\. e4 c6 2. Nf3 d5 3. Ne5 dxe4 4. Qh5 g6 5. Bc4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/InVfQ3xP/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_22.svg" alt="Chess Board for Trap #22" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_22.svg" alt="Win-Loss plot for Trap #22" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 30.9%
<br>
Probability of opponent playing into this position (including first move): 2.6%
<br>
Stockfish evaluation: -2.7. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/InVfQ3xP/white#9">https://lichess.org/InVfQ3xP/white#9</a>



#### Trap #23, Van Geet Opening

1\. Nc3 d5 2. e4 d4 3. Bb5+ c6 4. Bc4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/zj7lWGEz/white#7">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_23.svg" alt="Chess Board for Trap #23" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_23.svg" alt="Win-Loss plot for Trap #23" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 37.8%
<br>
Probability of opponent playing into this position (including first move): 9.3%
<br>
Stockfish evaluation: -4.2. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/zj7lWGEz/white#7">https://lichess.org/zj7lWGEz/white#7</a>



#### Trap #24, Slav Defense: Diemer Gambit

1\. e4 c6 2. d4 d5 3. c4 dxe4 4. Nc3 Nf6 5. Be2 Bf5 6. g4 Bg6 7. h4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6477qNPP/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_24.svg" alt="Chess Board for Trap #24" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_24.svg" alt="Win-Loss plot for Trap #24" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 32.5%
<br>
Probability of opponent playing into this position (including first move): 2.7%
<br>
Stockfish evaluation: -1.2. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6477qNPP/white#13">https://lichess.org/6477qNPP/white#13</a>



#### Trap #25, French Defense: Classical Variation, Steinitz Variation

1\. Nc3 e6 2. e4 d5 3. d4 Nf6 4. e5 Nfd7 5. Qh5 c5 6. Nf3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6kjAK9Re/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_25.svg" alt="Chess Board for Trap #25" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_25.svg" alt="Win-Loss plot for Trap #25" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 14.5%
<br>
Probability of opponent playing into this position (including first move): 1.6%
<br>
Stockfish evaluation: -0.8. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6kjAK9Re/white#11">https://lichess.org/6kjAK9Re/white#11</a>



#### Trap #26, French Defense: Schlechter Variation

1\. e4 e6 2. d4 d5 3. Bd3 Nf6 4. e5 Nfd7 5. Nf3 c5 6. Ng5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/buR8PZnI/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_26.svg" alt="Chess Board for Trap #26" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_26.svg" alt="Win-Loss plot for Trap #26" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 14.5%
<br>
Probability of opponent playing into this position (including first move): 1.7%
<br>
Stockfish evaluation: -1.0. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/buR8PZnI/white#11">https://lichess.org/buR8PZnI/white#11</a>



#### Trap #27, Caro-Kann Defense

1\. e4 c6 2. f4 d5 3. d3 dxe4 4. dxe4 Qxd1+ 5. Kxd1 Bg4+ 6. Ke1
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/03ty3x62/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_27.svg" alt="Chess Board for Trap #27" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_27.svg" alt="Win-Loss plot for Trap #27" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 22.0%
<br>
Probability of opponent playing into this position (including first move): 1.8%
<br>
Stockfish evaluation: +0.1. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/03ty3x62/white#11">https://lichess.org/03ty3x62/white#11</a>



#### Trap #28, French Defense: Schlechter Variation

1\. e4 e6 2. d4 d5 3. Bd3 Nf6 4. e5 Nfd7 5. f4 c5 6. f5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/n2x430LR/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_28.svg" alt="Chess Board for Trap #28" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_28.svg" alt="Win-Loss plot for Trap #28" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 15.8%
<br>
Probability of opponent playing into this position (including first move): 1.9%
<br>
Stockfish evaluation: -1.6. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/n2x430LR/white#11">https://lichess.org/n2x430LR/white#11</a>



#### Trap #29, Sicilian Defense

1\. e4 c5 2. Nf3 d6 3. d4 cxd4 4. e5 Nf6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6BIjxSNE/white#8">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_29.svg" alt="Chess Board for Trap #29" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_29.svg" alt="Win-Loss plot for Trap #29" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.0%
<br>
Probability of opponent playing into this position (including first move): 2.3%
<br>
Stockfish evaluation: +5.7. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6BIjxSNE/white#8">https://lichess.org/6BIjxSNE/white#8</a>



#### Trap #30, Italian Game: Two Knights Defense

1\. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. Qe2 Bc5 5. Ng5 O-O 6. Nxf7
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/2NvjbNfY/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_30.svg" alt="Chess Board for Trap #30" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_30.svg" alt="Win-Loss plot for Trap #30" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.0%
<br>
Probability of opponent playing into this position (including first move): 3.2%
<br>
Stockfish evaluation: -0.9. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/2NvjbNfY/white#11">https://lichess.org/2NvjbNfY/white#11</a>



#### Trap #31, Mieses Opening: Reversed Rat

1\. d3 e5 2. Bg5 Nc6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/bAyL0EY2/white#4">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_31.svg" alt="Chess Board for Trap #31" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_31.svg" alt="Win-Loss plot for Trap #31" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.1%
<br>
Probability of opponent playing into this position (including first move): 1.6%
<br>
Stockfish evaluation: +8.9. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/bAyL0EY2/white#4">https://lichess.org/bAyL0EY2/white#4</a>



#### Trap #32, Zukertort Opening: Tennison Gambit

1\. e4 d5 2. Nf3 dxe4 3. Ng5 Nf6 4. Nc3 Bf5 5. Bc4 e6 6. f3 exf3 7. Qxf3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/TzNPGCpX/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_32.svg" alt="Chess Board for Trap #32" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_32.svg" alt="Win-Loss plot for Trap #32" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 13.6%
<br>
Probability of opponent playing into this position (including first move): 1.3%
<br>
Stockfish evaluation: -1.9. Better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/TzNPGCpX/white#13">https://lichess.org/TzNPGCpX/white#13</a>



#### Trap #33, French Defense: Steiner Variation

1\. e4 e6 2. c4 d5 3. exd5 exd5 4. Qb3 dxc4 5. Bxc4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/yGNoUSPA/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_33.svg" alt="Chess Board for Trap #33" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_33.svg" alt="Win-Loss plot for Trap #33" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 28.2%
<br>
Probability of opponent playing into this position (including first move): 3.3%
<br>
Stockfish evaluation: +0.5. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/yGNoUSPA/white#9">https://lichess.org/yGNoUSPA/white#9</a>



#### Trap #34, English Opening: Agincourt Defense

1\. c4 e6 2. e3 d5 3. a3 dxc4 4. Nc3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/amxZKuDb/white#7">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_34.svg" alt="Chess Board for Trap #34" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_34.svg" alt="Win-Loss plot for Trap #34" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 11.1%
<br>
Probability of opponent playing into this position (including first move): 1.3%
<br>
Stockfish evaluation: -0.1. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/amxZKuDb/white#7">https://lichess.org/amxZKuDb/white#7</a>



#### Trap #35, King's Indian Attack: Symmetrical Defense

1\. Nf3 Nf6 2. g3 g6 3. e4 Bg7 4. e5 O-O 5. exf6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/pCIebZK9/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_35.svg" alt="Chess Board for Trap #35" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_35.svg" alt="Win-Loss plot for Trap #35" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 13.6%
<br>
Probability of opponent playing into this position (including first move): 2.7%
<br>
Stockfish evaluation: +4.6. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/pCIebZK9/white#9">https://lichess.org/pCIebZK9/white#9</a>



#### Trap #36, French Defense: Steinitz Attack

1\. e4 e6 2. e5 d5 3. Bb5+ Bd7 4. Be2
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/5YXqp02P/white#7">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_36.svg" alt="Chess Board for Trap #36" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_36.svg" alt="Win-Loss plot for Trap #36" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.7%
<br>
Probability of opponent playing into this position (including first move): 1.3%
<br>
Stockfish evaluation: -0.6. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/5YXqp02P/white#7">https://lichess.org/5YXqp02P/white#7</a>



#### Trap #37, Mieses Opening

1\. d3 Nf6 2. g3 g6 3. Bg2 Bg7 4. f4 O-O 5. Nh3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/nZKtuH7g/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_37.svg" alt="Chess Board for Trap #37" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_37.svg" alt="Win-Loss plot for Trap #37" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 24.7%
<br>
Probability of opponent playing into this position (including first move): 3.2%
<br>
Stockfish evaluation: -0.8. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/nZKtuH7g/white#9">https://lichess.org/nZKtuH7g/white#9</a>



#### Trap #38, Horwitz Defense

1\. d4 e6 2. Nf3 d5 3. c3 Nf6 4. Bg5 Be7 5. Bxf6 Bxf6 6. Qc2
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Lxqsm1s4/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_38.svg" alt="Chess Board for Trap #38" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_38.svg" alt="Win-Loss plot for Trap #38" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.8%
<br>
Probability of opponent playing into this position (including first move): 1.3%
<br>
Stockfish evaluation: -0.4. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Lxqsm1s4/white#11">https://lichess.org/Lxqsm1s4/white#11</a>



#### Trap #39, Mieses Opening

1\. d3 e6 2. g3 d5 3. Bg2 Nf6 4. f4 Be7 5. Nh3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Y7p9wZKk/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_39.svg" alt="Chess Board for Trap #39" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_39.svg" alt="Win-Loss plot for Trap #39" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.3%
<br>
Probability of opponent playing into this position (including first move): 1.2%
<br>
Stockfish evaluation: -0.8. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Y7p9wZKk/white#9">https://lichess.org/Y7p9wZKk/white#9</a>



#### Trap #40, Indian Defense

1\. d4 Nf6 2. Bf4 g6 3. Nc3 Bg7 4. e4 d6 5. e5 dxe5 6. dxe5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/9HXQ2uBp/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_40.svg" alt="Chess Board for Trap #40" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_40.svg" alt="Win-Loss plot for Trap #40" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.2%
<br>
Probability of opponent playing into this position (including first move): 2.6%
<br>
Stockfish evaluation: +0.7. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/9HXQ2uBp/white#11">https://lichess.org/9HXQ2uBp/white#11</a>



#### Trap #41, Nimzo-Larsen Attack

1\. b3 e6 2. Nf3 d5 3. Bb2 Nf6 4. Nc3 Be7 5. e4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6chpKtSj/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_41.svg" alt="Chess Board for Trap #41" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_41.svg" alt="Win-Loss plot for Trap #41" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 15.4%
<br>
Probability of opponent playing into this position (including first move): 1.5%
<br>
Stockfish evaluation: -0.9. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/6chpKtSj/white#9">https://lichess.org/6chpKtSj/white#9</a>



#### Trap #42, Caro-Kann Defense: Tartakower Variation

1\. e4 c6 2. d4 d5 3. Nd2 dxe4 4. Nxe4 Nf6 5. Nxf6+ exf6 6. Bd3 Bd6 7. Qh5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/TwmNBJuJ/white#13">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_42.svg" alt="Chess Board for Trap #42" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_42.svg" alt="Win-Loss plot for Trap #42" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 19.9%
<br>
Probability of opponent playing into this position (including first move): 1.6%
<br>
Stockfish evaluation: +0.3. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/TwmNBJuJ/white#13">https://lichess.org/TwmNBJuJ/white#13</a>



#### Trap #43, Zukertort Opening: Kingside Fianchetto

1\. Nf3 g6 2. e4 Bg7 3. Nc3 e6 4. d4 Ne7 5. h4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/EAXaU1Oe/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_43.svg" alt="Chess Board for Trap #43" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_43.svg" alt="Win-Loss plot for Trap #43" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 15.2%
<br>
Probability of opponent playing into this position (including first move): 1.0%
<br>
Stockfish evaluation: +1.4. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/EAXaU1Oe/white#9">https://lichess.org/EAXaU1Oe/white#9</a>



#### Trap #44, French Defense: Steiner Variation

1\. c4 e6 2. e4 d5 3. cxd5 exd5 4. Qa4+ Bd7 5. Qb3
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Y8TGJNlm/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_44.svg" alt="Chess Board for Trap #44" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_44.svg" alt="Win-Loss plot for Trap #44" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 23.1%
<br>
Probability of opponent playing into this position (including first move): 2.7%
<br>
Stockfish evaluation: -1.0. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/Y8TGJNlm/white#9">https://lichess.org/Y8TGJNlm/white#9</a>



#### Trap #45, Van Geet Opening

1\. Nc3 Nf6 2. d4 g6 3. Bg5 Bg7 4. e4 d6 5. e5
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/g974dDEh/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_45.svg" alt="Chess Board for Trap #45" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_45.svg" alt="Win-Loss plot for Trap #45" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.9%
<br>
Probability of opponent playing into this position (including first move): 2.1%
<br>
Stockfish evaluation: +0.1. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/g974dDEh/white#9">https://lichess.org/g974dDEh/white#9</a>



#### Trap #46, Hungarian Opening: Catalan Formation

1\. g3 e6 2. Bg2 d5 3. e4 dxe4 4. Ne2 Nf6 5. O-O
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/34oIebFC/white#9">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_46.svg" alt="Chess Board for Trap #46" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_46.svg" alt="Win-Loss plot for Trap #46" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 11.5%
<br>
Probability of opponent playing into this position (including first move): 1.1%
<br>
Stockfish evaluation: -1.0. Slightly better for black with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/34oIebFC/white#9">https://lichess.org/34oIebFC/white#9</a>



#### Trap #47, French Defense: Chigorin Variation

1\. e4 e6 2. Qe2 d5 3. exd5 Qxd5 4. Nc3 Qd8 5. b3 Nf6 6. Bb2 Be7 7. O-O-O O-O 8. g4
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/wjePsK9H/white#15">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_47.svg" alt="Chess Board for Trap #47" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_47.svg" alt="Win-Loss plot for Trap #47" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 12.0%
<br>
Probability of opponent playing into this position (including first move): 1.4%
<br>
Stockfish evaluation: +1.1. Slightly better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/wjePsK9H/white#15">https://lichess.org/wjePsK9H/white#15</a>



#### Trap #48, Van Geet Opening: Dunst-Perrenet Gambit

1\. e4 d5 2. d3 dxe4 3. Nc3 exd3 4. Bxd3 Nf6 5. Qe2 e6
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/ObRvVBfM/white#10">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_48.svg" alt="Chess Board for Trap #48" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_48.svg" alt="Win-Loss plot for Trap #48" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 10.8%
<br>
Probability of opponent playing into this position (including first move): 1.1%
<br>
Stockfish evaluation: 0.0. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/ObRvVBfM/white#10">https://lichess.org/ObRvVBfM/white#10</a>



#### Trap #49, Nimzo-Larsen Attack: Indian Variation

1\. b3 Nf6 2. Bb2 g6 3. d3 Bg7 4. Bxf6 O-O 5. Bxg7 Kxg7
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/B2eNhsmS/white#10">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_49.svg" alt="Chess Board for Trap #49" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_49.svg" alt="Win-Loss plot for Trap #49" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 11.0%
<br>
Probability of opponent playing into this position (including first move): 1.6%
<br>
Stockfish evaluation: +6.7. Better for white with perfect play
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/B2eNhsmS/white#10">https://lichess.org/B2eNhsmS/white#10</a>



#### Trap #50, Hungarian Opening: Indian Defense

1\. g3 Nf6 2. Bg2 g6 3. e4 Bg7 4. e5 Ng8 5. Nf3 d6 6. Qe2
<br>
<a target="_blank" rel="noopener noreferrer" href="https://lichess.org/HmDbYBLM/white#11">
<img src = "{{site.baseurl}}/assets/white_svg_boards/board_50.svg" alt="Chess Board for Trap #50" width="350"/>
</a>
<br>
<img src = "{{site.baseurl}}/assets/white_svg_boards/barplot_50.svg" alt="Win-Loss plot for Trap #50" width="350"/>
<br>
Probability of opponent playing into this position (excluding first move): 14.2%
<br>
Probability of opponent playing into this position (including first move): 1.5%
<br>
Stockfish evaluation: +0.4. Roughly even
<br>
Analysis board: <a target="_blank" rel="noopener noreferrer" href="https://lichess.org/HmDbYBLM/white#11">https://lichess.org/HmDbYBLM/white#11</a>



