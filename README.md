# X-Order-Markov-Chain-Procedural-Epithet-Generation
Generating Fantasy Epithets using Markov Chains

![fantasy_painting](images/landscape.jpg)

## Why
I'm an amateur fantasy writer with a terrible imagination. I need some way to create epithets without working hard. This seems like a good time to use Markov Chains.

## How will this work?
We're going to be using Markov Chains to generate epithets procedurally. If you want to read more about how Markov Chains work, check out this [documentation](http://pcg.wikidot.com/pcg-algorithm:markov-chain) on Markov Chains.



## Roadmap 
~~Strikethrough indicates status is finished~~
- ~~Add basic project info to README~~
- ~~Disable push to default branch~~
- ~~Add pull_request_template~~
- ~~Set up CI through GitHub Actions~~
	- ~~install virtualenv in CI~~
	- ~~Add linter to CI~~
	- ~~Add unit tests to CI~~
- ~~Add Flake8 linting locally~~
- ~~Add unit tests locally~~
- ~~Add virtual environment for Python locally~~
- Code Markov Chain Generator
- Scrape Data
	- Game of Thrones Epithets
	- Backed by weighted Dictionary Chains
- Expand data set through manual filtering

## Design
- Markov Chain Class:
  - Iterate through words
    - Each letter adds to count of letter at index/level X
    - [Weighted random choice](https://docs.python.org/3/library/random.html#random.choices) from (letter, count) in level
- Wrapper around Markov Chain Class:
  - Create chains for backup, GOT + custom
  - Logic behind what to do when getting stuck
  - How long chain should be
  - When to use backup
- [sqlite3 DB](https://docs.python.org/3/library/sqlite3.html)
	- Store Game of Thrones Epithets
	- Store backup dictionary
	- Store Custom Epithets
	- Epithet, type(custom, backup, GOT)
