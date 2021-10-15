

| Installation from pip | Build From Source |
| --- | --- |
| Install feature which already built from source, including general features and preset parameters | Can select own features and parameters to be installed |
| Install at default location| Developer specify the install location |
| Might run slower because hidden conflicts between features| Can set the opmitization flags to built a fast performance lib |
| Cannot add nor remove feature from prebuilt| Developer can add or remove feaures/library to optimize performance |
| Programmer does not expected to have knowledge about library| Programmer must have strong knowledge about library |
| Package manager will take care of package updation| Programmer have responsible for updating which part of library, security, compatible update,... |


So when to build dependencies (i.e: OpenCV) from source ?
- When we need to run libs in production environment. Most of the time, we only use some operation/feature hence do not need to install full library. This will also save memory and achieve faster performance
- When we need some modification/optimization on the library parameters 
- Due to copyrights, some function are only possible if you built OpenCV from source


Reference sources: 
https://cv-tricks.com/how-to/installation-of-opencv-4-1-0-in-windows-10-from-source/