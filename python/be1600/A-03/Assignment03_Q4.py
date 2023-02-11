room = {
  "CS101":3004,
  "CS102":4501,
  "CS103":6755,
  "NT110":1244,
  "CM241":1411,
}

instructor = {
  "CS101":"Haynes",
  "CS102":"Alvarado",
  "CS103":"Rich",
  "NT110":"Burke",
  "CM241":"Lee",
}

time = {
  "CS101":"8:00 a.m.",
  "CS102":"9:00 a.m.",
  "CS103":"10:00 a.m.",
  "NT110":"11:00 a.m.",
  "CM241":"1:00 p.m.",
}

x = input("Enter a course number: ")

if (x in room) and (x in instructor) and (x in time):
  print("The details for course", x, "are:")
  print("Room:", room[x])
  print("Instructor:", instructor[x])
  print("Time: ", time[x])
else:
  print(x, "is an invalid course number")