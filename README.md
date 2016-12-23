# Up to date exchange rates
CLI to get exchange rates.

## requirementes
- Python 3.5

## To use this tool
- clone this repo

## commands
- `--list` or `-l` to list available currency operators
- `--currency` or `-c` with `currency operator`
- `--symbols` or `-s` with currencies concatenated with `,` to get specific exchange rate for those 2 currencies

All availabel currencies are listed by running with `--list` or `-l`

### examples
`python3.5 main.py --currency EUR` will return the exchange rate against the Euro
`python3.5 main.py --symbols EUR,USD` will only return the exchange rate of the USD against the Euro

Only works when http://fixer.io/ is up and running.
