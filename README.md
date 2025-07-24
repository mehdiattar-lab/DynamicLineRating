# DynamicLineRating
The Wrapper.py code is a plug-and-play script that reads data from two CSV files (e.g., for wind speed and temperature) and performs DLR analysis of overhead transmission line.
The condoctor characteristics should be modified in the condoctor.py file.
The wrapper.py can utilize DLR calculation based on IEEE 738 standard or CIGRE 601 standard, depending on what the user wants (currently it is coded to utilize the IEEE standard). Both standards are almost identical, with minor differences.


For users:
Pull the code in your local repo.
Modify the content of conductor.py according to the specifications of the transmission line conductor.
For the location where the transmission line is located, you need weather data in CSV format.
For the worst-case scenario, you can assume that the conductor temperature is maximum, and then, based on ambient temperature and wind speed, calculate how much current could flow.
If you have power flow results, you can utilize the transmission line current, make the thermodynamic model of the line to calculate its temperature, and use that temperature as input to the IEEE standard. This part has only been partly implemented (power flow is missing) and therefore it is commented out at the end of the wrapper code. 
Run Wrapper.py and see the outcomes. Currently, the wrapper also plots the outcomes of the test scenario. 


## Acknowledgments

The IEEE738.py, cigre604.py code is pulled from https://github.com/tommz9/pylinerating.git, licensed under APACHE-02, and has been used with no changes.
The nusselt.py and conductor.py code is pulled from https://github.com/tommz9/pylinerating.git, licensed under APACHE-02, and has been used with some parameter changes.

