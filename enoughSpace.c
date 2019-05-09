//"Will there be enough space?"
int enough(int cap, int on, int wait)
{
  
  int roomLeft = cap - on;
  
  if(roomLeft < wait){
    
    int cantFit = roomLeft - wait;
    return -cantFit;
    
  }
  
  else return 0;

}