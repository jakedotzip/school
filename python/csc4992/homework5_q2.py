from breezypythongui import EasyFrame
 
  
class RandomProg(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Random Program")
  
        # Label and field for the income
        self.addLabel(text = "Enter starting number",
                      row = 0, column = 0)
        self.startField = self.addIntegerField(value = 0, 
                                              row = 0,
                                              column = 1)
 
        # Label and field for the number of dependents
        self.addLabel(text = "Enter ending number",
                      row = 1, column = 0)
        self.endField = self.addIntegerField(value = 0,
                                             row = 1,
                                             column = 1)
  
        # Label and field for the exemption amount
        self.addLabel(text = "Increment value",
                      row = 2, column = 0)
        self.increField = self.addIntegerField(value = 0,
                                           row = 2,
                                           column = 1)
        # The command button
        self.addButton(text = "Run", row = 3, column = 0,
                       columnspan = 2, command = self.runProg)

        self.addLabel(text = "Output", row = 4, column=0)
        self.outputArea = self.addTextArea(text = "", row = 5, column=0)

        self.addLabel(text = "Loop times", row = 6, column=0, rowspan = 10)
        self.countField = self.addIntegerField(value = 0, row = 6, column = 1)
  
    # The event handler method for the button
    def runProg(self):
        try:
          startValue = self.startField.getNumber()        
          endValue = self.endField.getNumber()        
          increValue = self.increField.getNumber()
          # throw error accordingly
          if startValue > 200 or startValue < 135:
              self.messageBox(title="ERROR!", message= "Starting value must be between 135 and 200")
          elif endValue > 95 or endValue < 62:
            self.messageBox(title="ERROR!", message= "Ending value must be between 62 and 95")
          elif increValue > 5 or increValue < 2:
            self.messageBox(title="ERROR!", message= "Increment value must be between 2 and 5")
          else:
            for i in range(startValue,endValue-increValue,-increValue):
              if i == startValue:  #this will ignore the first number of the list
                self.outputArea.appendText(str(i) + ' ')
                count = 0           
              else:
                count+=1    #increase by 1 each time the program makes a loop
                self.outputArea.appendText(str(i) + ' ')
            self.countField.setNumber(count)
        except ValueError:
          self.messageBox(title="ERROR!", message="Input must be an integer!")
 
#Instantiate and pop up the window.
def main():
  RandomProg().mainloop()

if __name__ == "__main__":
  main()