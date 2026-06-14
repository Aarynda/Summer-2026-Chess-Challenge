# Week 1: 5/28/2026 - 5/31/2026
## Ideation Phase
The very first phase of this project is going to be the research phase, starting with researching standard chess notation for user input/output, as well as sketching out basic ideas for the terminal interface.

### Research - Chess notation
(Summarized from the Wikipedia article on Algebraic Notation - https://en.wikipedia.org/wiki/Algebraic_notation_(chess) )

Basic algebraic notation uses letters to indicate each piece, as well as grid notation to indicate where the piece moves to.



### Ideas
The overall format required for this challenge immediately makes me think of a terminal application - I want to be able to implement a custom terminal and parse user inputs as commands in a consistent game loop.
The main terminal needs to accommodate the import/export/game start/game continue/rendering menu, and then a main game loop needs to support the commands for movement, listing all available moves, rejection of invalid moves, and edge cases generated in game play.