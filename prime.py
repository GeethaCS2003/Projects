#include <iostream>

using namespace std;



enum Genre {ACTION, COMEDY, DRAMA, ROMANCE, THRILLER};



class Time { 

public:

    int h;

    int m;

};



class Movie { 

public: 

    string title;

    Genre genre;     // only one genre per movie

    int duration;    // in minutes

};



class TimeSlot { 

public: 

    Movie movie;     // what movie

    Time startTime;  // when it starts



};



int minutesSinceMidnight(Time time)

{

    int min = (time.h * 60) + time.m;

    return min;

}



int minutesUntil(Time earlier, Time later)

{

    int e_min = minutesSinceMidnight(earlier);

    int l_min = minutesSinceMidnight(later);



    

    int dif =l_min-e_min;

    return dif;

}



Time addMinutes(Time time0, int min)

{

    Time now;

    int mins_hr = minutesSinceMidnight(time0) + min;

    now.h = mins_hr / 60;

    now.m = mins_hr % 60;



    return now;

}                      
