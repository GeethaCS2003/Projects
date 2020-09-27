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



...

[Message clipped]  View entire message





Lakshmi Palchuri 

12:30 PM (53 minutes ago)



to me 







#include <iostream>

#include <vector>

using namespace std;



vector<int> sumPairWise(vector<int> &v1, vector<int> &v2)

{

    if (v1.empty() && !v2.empty())

    {

        return v2;

    }

    //if v1 only is empty the return v2

    else if (v2.empty() && !v1.empty())

    {

        return v1;

    }

    //if v2 only is empty the return v1

    else if(v1.size() == v2.size())

    {

        vector<int> nums;



        for (int j = 0; j < v2.size(); j++)

        {

            nums.push_back(v1[j] + v2[j]);

        }

        return nums;

    }

    //if v1 and v2 have the same sizes then perform

    //pairwise sum based on index with each vector

    else if(v1.size() < v2.size())

    {

        int x = (v2.size() - v1.size()) + 1;

        vector<int> nums;

        for (int i = 0; i < x; i++)

        {

            v1.push_back(0);

        }



        for (int j = 0; j < v2.size(); j++)

        {

            nums.push_back(v1[j] + v2[j]);

        }

        return nums;

    }

    //if v2 has a larger size then add 0's to v1 

    //have the same size as v2 and the add pairwise sum

    //acordingly 

    else if(v1.size() > v2.size())

    {

        vector<int> nums2;

        int y = v1.size() - v2.size();                          
