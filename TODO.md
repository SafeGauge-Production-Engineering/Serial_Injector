
# GOAL: To insert serial number from a list into the bluetooth profile

## TODO Items


## Steps
```
1. Get serial numbers in as a list (from test.csv for starters)
2. Iterate through the list
3. Inject serial number
4. Overwrite the previous file so the new one is saved there
5. Call the BT programmer to start? Rewrite the programmer?

```

## Questions
- How should we get it to start programming?
- How can we bypass / redo the BT programmer software to do it as soon as there's a connection?

## Resources To Use
- Spyder IDE

## Future Upgrades
- Input from arduino pro micr as USB host controlled by foot pedal (with next )
  - Start by getting the pedal/buttons to go back and forward through the list of serial numbers
  - Ability to select serial number to program (then does it automatically from there)
    - This allows you to go back through the batch and reprogram the selected serial
    - Scanning barcodes in future
    
## Issues
- Module Import error - searching in the wrong place or not added to path
    - in Spyder the path needs to be added to its specific path [Tools>>PythonPath Manger]