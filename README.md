# concatcsv
concatenates csv files

## Usage

`./concat.py /path/to/your/csvfiles`

This will create a `concat.csv` file in the script directory that combines all the csv files into one.

## Example

`./concat.py ./testdata`

### Result

**concat.csv**
```csv
Username; Identifier;First name;Last name
brian01; brian01; Brian; O'Connell
james01; james01; James; O'Connell
jen01; jen01; Jennifer; O'Connell
luke01; luke01; Luke; O'Connell
mike01; mike01; Mike; O'Connell
taylor10;9013;Taylor;Swift
olivia09;2071;Olivia;Rodrigo
timber01;2072;Justin;Timberlake
wknd02;2073;The;Weekend
harry01;2071;Harry;Styles
booker12;9012;Rachel;Booker
grey07;2070;Laura;Grey
johnson81;4081;Craig;Johnson
jenkins46;9346;Mary;Jenkins
smith79;5079;Jamie;Smith
```

### Test files

**testdata/username.csv**
```csv
Username; Identifier;First name;Last name
booker12;9012;Rachel;Booker
grey07;2070;Laura;Grey
johnson81;4081;Craig;Johnson
jenkins46;9346;Mary;Jenkins
smith79;5079;Jamie;Smith
```

**testdata/username2.csv**
```csv
Username; Identifier;First name;Last name
taylor10;9013;Taylor;Swift
olivia09;2071;Olivia;Rodrigo
timber01;2072;Justin;Timberlake
wknd02;2073;The;Weekend
harry01;2071;Harry;Styles
```

**testdata/username3.csv**
```csv
Username; Identifier;First name;Last name
brian01; brian01; Brian; O'Connell
james01; james01; James; O'Connell
jen01; jen01; Jennifer; O'Connell
luke01; luke01; Luke; O'Connell
mike01; mike01; Mike; O'Connell
```
