
# GOAL: To insert serial number from a list into the bluetooth profile

## TODO Items
- Add new gatt_sensor.xml file - https://www.projectpro.io/recipes/create-and-delete-file-in-python
- Pull serial numbers from a test bank
- Remove previous (or overwrite current in that path)
- Iterate through the list of serial numbers

## Steps
```
1. Get serial numbers in as a list (from test.csv for starters)
2. Iterate through the list
3. [Make a new file and insert all info , concatenating new serial number in there] / [Edit current file]
4. Overwrite the previous file so the new one is saved there
5. Call the BT programmer to start? Rewrite tehe programmer?

```

## Questions
- How should we get it to start programming?
- How can we bypass / redo the BT programmer software to do it as soon as there's a connection?

## Resources To Use
- Use Spyder IDE

## Future Upgrades
- Input from arduino pro micr as USB host controlled by foot pedal (with next )
  - Start by getting the pedal/buttons to go back and forward through the list of serial numbers
  - Ability to select serial number to program (then does it automatically from there)
    - This allows you to go back through the batch and reprogram the selected serial