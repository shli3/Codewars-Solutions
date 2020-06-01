function XO(str) {
    var x = 0;
    var o = 0;
    var len = str.length;
    if(len == 0) return true;
    var counter = 0;
    
    while(counter != len)
    {
      if(str.charAt(counter) == 'x' || str.charAt(counter) == 'X') x++;
      else if(str.charAt(counter) == 'o' || str.charAt(counter) == 'O') o++;
      counter++;
    }
    
    if(x == o) return true;
    else return false;
    
}
