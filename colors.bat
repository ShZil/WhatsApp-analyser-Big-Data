@Echo off
Setlocal
::EchoANSI.cmd
cls
:: Display a sample of all the ANSI colours.
:: Requires windows 1909 or newer

:: Define foreground and background ANSI colors:
Set _fBlack=[30m
Set _bBlack=[40m
Set _fRed=[31m
Set _bRed=[41m
Set _fGreen=[32m
Set _bGreen=[42m
Set _fYellow=[33m
Set _bYellow=[43m
Set _fBlue=[34m
Set _bBlue=[44m
Set _fMag=[35m
Set _bMag=[45m
Set _fCyan=[36m
Set _bCyan=[46m
Set _fLGray=[37m
Set _bLGray=[47m
Set _fDGray=[90m
Set _bDGray=[100m
Set _fBRed=[91m
Set _bBRed=[101m
Set _fBGreen=[92m
Set _bBGreen=[102m
Set _fBYellow=[93m
Set _bBYellow=[103m
Set _fBBlue=[94m
Set _bBBlue=[104m
Set _fBMag=[95m
Set _bBMag=[105m
Set _fBCyan=[96m
Set _bBCyan=[106m
Set _fBWhite=[97m
Set _bBWhite=[107m
Set _RESET=[0m

Echo %_RESET% Black foreground 30
Echo %_fBlack%%_bRed% Black/Red  %_fBlack%%_bGreen%Black/Green %_fBlack%%_bYellow%Black/Yellow %_fBlack%%_bBlue% Black/Blue   %_fBlack%%_bMag%Black/Magenta %_fBlack%%_bCyan% Black/Cyan  %_fBlack%%_bLGray%Black/lGray
Echo %_fBlack%%_bDGray%Black/dGray %_fBlack%%_bBRed% Black/lRed %_fBlack%%_bBGreen%Black/lGreen %_fBlack%%_bBYellow%Black/lYellow %_fBlack%%_bBBlue% Black/lBlue  %_fBlack%%_bBMag%Black/lMagenta %_fBlack%%_bBCyan%Black/lCyan %_fBlack%%_bBWhite%Black/White
Echo %_RESET% Red foreground 31
Echo %_fRed%%_bBlack% Red/Black %_fRed%%_bGreen% Red/Green %_fRed%%_bYellow% Red/Yellow %_fRed%%_bBlue% Red/Blue %_fRed%%_bMag% Red/Magenta %_fRed%%_bCyan% Red/Cyan   %_fRed%%_bLGray% Red/lGray
Echo %_fRed%%_bDGray% Red/dGray %_fRed%%_bBRed% Red/lRed %_fRed%%_bBGreen% Red/lGreen %_fRed%%_bBYellow% Red/lYellow %_fRed%%_bBBlue% Red/lBlue %_fRed%%_bBMag% Red/lMagenta %_fRed%%_bBCyan% Red/lCyan %_fRed%%_bBWhite% Red/White
Echo %_RESET% Green foreground 32
Echo %_fGreen%%_bBlack%Green/Black %_fGreen%%_bRed% Green/red %_fGreen%%_bYellow%Green/Yellow  %_fGreen%%_bBlue% Green/Blue   %_fGreen%%_bMag%Green/Magenta %_fGreen%%_bCyan%Green/Cyan %_fGreen%%_bLGray%Green/lGray
Echo %_fGreen%%_bDGray%Green/dGray %_fGreen%%_bBRed%Green/lRed %_fGreen%%_bBGreen% Green/lGreen %_fGreen%%_bBYellow%Green/lYellow %_fGreen%%_bBBlue% Green/lBlue  %_fGreen%%_bBMag%Green/lMagenta %_fGreen%%_bBCyan%Green/lCyan %_fGreen%%_bBWhite%Green/White
Echo %_RESET% Yellow foreground 33
Echo %_fYellow%%_bBlack%Yellow/Black %_fYellow%%_bRed%Yellow/Red  %_fYellow%%_bGreen%Yellow/Green  %_fYellow%%_bBlue% Yellow/Blue   %_fYellow%%_bMag%Yellow/Magenta %_fYellow%%_bCyan%Yellow/Cyan %_fYellow%%_bLGray%Yellow/lGray
Echo %_fYellow%%_bDGray%Yellow/dGray %_fYellow%%_bBRed%Yellow/lRed %_fYellow%%_bBGreen%Yellow/lGreen %_fYellow%%_bBYellow%Yellow/lYellow %_fYellow%%_bBBlue% Yellow/lBlue  %_fYellow%%_bBMag%YellowlMagenta %_fYellow%%_bBCyan%Yellow/lCyan %_fYellow%%_bBWhite%Yellow/White
Echo %_RESET% Blue foreground 34
Echo %_fBlue%%_bBlack% Blue/Black %_fBlue%%_bRed% Blue/Red  %_fBlue%%_bGreen% Blue/Green %_fBlue%%_bYellow% Blue/Yellow   %_fBlue%%_bMag% Blue/Magenta %_fBlue%%_bCyan% Blue/Cyan %_fBlue%%_bLGray% Blue/lGray
Echo %_fBlue%%_bDGray% Blue/dGray %_fBlue%%_bBRed% Blue/lRed %_fBlue%%_bBGreen% Blue/lGreen %_fBlue%%_bBYellow% Blue/lYellow %_fBlue%%_bBBlue% Blue/lBlue   %_fBlue%%_bBMag% Blue/lMagenta %_fBlue%%_bBCyan% Blue/lCyan %_fBlue%%_bBWhite% Blue/White
Echo %_RESET% Magenta foreground 35
Echo %_fMag%%_bBlack%Magenta/Black %_fMag%%_bRed%Magenta/Red  %_fMag%%_bGreen% Magenta/Green %_fMag%%_bYellow%Magenta/Yellow  %_fMag%%_bBlue% Magenta/Blue %_fMag%%_bCyan% Magenta/Cyan %_fMag%%_bLGray%Magenta/lGray
Echo %_fMag%%_bDGray%Magenta/dGray %_fMag%%_bBRed%Magenta/lRed %_fMag%%_bBGreen%Magenta/lGreen %_fMag%%_bBYellow%Magenta/lYellow %_fMag%%_bBBlue%Magenta/lBlue %_fMag%%_bBMag%Magenta/lMagenta %_fMag%%_bBCyan%Magenta/lCyan %_fMag%%_bBWhite%Magenta/White
Echo %_RESET% Cyan foreground 36
Echo %_fCyan%%_bBlack% Cyan/Black  %_fCyan%%_bRed% Cyan/Red  %_fCyan%%_bGreen% Cyan/Green  %_fCyan%%_bYellow% Cyan/Yellow %_fCyan%%_bBlue% Cyan/Blue  %_fCyan%%_bMag% Cyan/Magenta  %_fCyan%%_bLGray% Cyan/lGray 
Echo %_fCyan%%_bDGray% Cyan/dGray  %_fCyan%%_bBRed%Cyan/lRed  %_fCyan%%_bBGreen%Cyan/lGreen  %_fCyan%%_bBYellow%Cyan/lYellow %_fCyan%%_bBBlue%Cyan/lBlue  %_fCyan%%_bBMag%Cyan/lMagenta  %_fCyan%%_bBCyan%Cyan/lCyan  %_fCyan%%_bBWhite%Cyan/White
Echo %_RESET% LightGray foreground 37 (lGray)
Echo %_fLGray%%_bBlack%lGray/Black %_fLGray%%_bRed%lGray/Red  %_fLGray%%_bGreen% lGray/Green %_fLGray%%_bYellow% lGray/Yellow %_fLGray%%_bBlue% lGray/Blue %_fLGray%%_bMag% lGray/Magenta %_fLGray%%_bCyan% lGray/Cyan
Echo %_fLGray%%_bDGray%lGray/dGray %_fLGray%%_bBRed%lGray/lRed %_fLGray%%_bBGreen%lGray/lGreen %_fLGray%%_bBYellow%lGray/lYellow %_fLGray%%_bBBlue%lGray/lBlue %_fLGray%%_bBMag%lGray/lMagenta %_fLGray%%_bBCyan%lGray/lCyan %_fLGray%%_bBWhite%lGray/White
Echo %_RESET% Dark Gray foreground 90 (dGray)
Echo %_fDGray%%_bBlack% dGray/Black %_fDGray%%_bRed% dGray/Red   %_fDGray%%_bGreen% dGray/Green  %_fDGray%%_bYellow%dGray/Yellow %_fDGray%%_bBlue% dGray/Blue    %_fDGray%%_bMag%dGray/Magenta %_fDGray%%_bCyan%dGray/Cyan %_fDGray%%_bLGray%dGray/lGray
Echo %_fDGray%%_bBRed%d Gray/lRed  %_fDGray%%_bBGreen%dGray/lGreen %_fDGray%%_bBYellow%dGray/lYellow %_fDGray%%_bBBlue% dGray/lBlue %_fDGray%%_bBMag%dGray/lMagenta %_fDGray%%_bBCyan% dGray/lCyan  %_fDGray%%_bBWhite%dGray/White
Echo %_RESET% Light Red foreground 91 (lRed)
Echo %_fBRed%%_bBlack% lRed/Black %_fBRed%%_bRed%  lRed/Red   %_fBRed%%_bGreen% lRed/Green   %_fBRed%%_bYellow% lRed/Yellow %_fBRed%%_bBlue% lRed/Blue %_fBRed%%_bMag% lRed/Magenta %_fBRed%%_bCyan% lRed/Cyan %_fBRed%%_bLGray% lRed/lGray
Echo %_fBRed%%_bDGray% lRed/dGray %_fBRed%%_bBGreen% lRed/lGreen %_fBRed%%_bBYellow% lRed/lYellow %_fBRed%%_bBBlue% lRed/lBlue  %_fBRed%%_bBMag% lRed/lMagenta %_fBRed%%_bBCyan% lRed/lCyan %_fBRed%%_bBWhite% lRed/White
Echo %_RESET% Light Green foreground 92 (lGreen)
Echo %_fBGreen%%_bBlack%lGreen/Black %_fBGreen%%_bRed% lGreen/Red %_fBGreen%%_bGreen% lGreen/Green  %_fBGreen%%_bYellow%lGreen/Yellow %_fBGreen%%_bBlue% lGreen/Blue  %_fBGreen%%_bMag%lGreen/Magenta %_fBGreen%%_bCyan%lGreen/Cyan %_fBGreen%%_bLGray%lGreen/lGray
Echo %_fBGreen%%_bDGray%lGreen/dGray %_fBGreen%%_bBRed%lGreen/lRed %_fBGreen%%_bBYellow%lGreen/lYellow %_fBGreen%%_bBBlue% lGreen/lBlue %_fBGreen%%_bBMag%lGreen/lMagenta %_fBGreen%%_bBCyan%lGreen/lCyan %_fBGreen%%_bBWhite%lGreen/White
Echo %_RESET% Light yellow foreground 93 (lYellow)
Echo %_fBYellow%%_bBlack%lYellow/Black %_fBYellow%%_bRed% lYellow/Red %_fBYellow%%_bGreen% lYellow/Green %_fBYellow%%_bYellow%lYellow/Yellow %_fBYellow%%_bBlue% lYellow/Blue   %_fBYellow%%_bMag%lYellow/Magenta %_fBYellow%%_bCyan%lYellow/Cyan %_fBYellow%%_bLGray%lYellow/lGray
Echo %_fBYellow%%_bDGray%lYellow/dGray %_fBYellow%%_bBRed%lYellow/lRed %_fBYellow%%_bBGreen%lYellow/lGreen %_fBYellow%%_bBBlue% lYellow/lBlue %_fBYellow%%_bBMag%lYellow/lMagenta %_fBYellow%%_bBCyan%lYellow/lCyan %_fBYellow%%_bBWhite%lYellow/White
Echo %_RESET% Light blue foreground 94 (lBlue)
Echo %_fBBlue%%_bBlack% lBlue/Black %_fBBlue%%_bRed% lBlue/Red  %_fBBlue%%_bGreen% lBlue/Green  %_fBBlue%%_bYellow% lBlue/Yellow  %_fBBlue%%_bBlue%  lBlue/Blue   %_fBBlue%%_bMag% lBlue/Magenta %_fBBlue%%_bCyan% lBlue/Cyan %_fBBlue%%_bLGray% lBlue/lGray
Echo %_fBBlue%%_bDGray% lBlue/dGray %_fBBlue%%_bBRed% lBlue/lRed %_fBBlue%%_bBGreen% lBlue/lGreen %_fBBlue%%_bBYellow% lBlue/lYellow %_fBBlue%%_bBMag% lBlue/lMagenta %_fBBlue%%_bBCyan% lBlue/lCyan %_fBBlue%%_bBWhite% lBlue/White
Echo %_RESET% Light Magenta foreground 95 (lMagenta)
Echo %_fBMag%%_bBlack%lMagenta/Black %_fBMag%%_bRed% lMagenta/Red %_fBMag%%_bGreen% lMagenta/Green %_fBMag%%_bYellow%lMagenta/Yello %_fBMag%%_bBlue%lMagenta/Blue %_fBMag%%_bMag%lMagenta/Magenta %_fBMag%%_bCyan%lMagenta/Cyan %_fBMag%%_bLGray%lMagenta/lGray
Echo %_fBMag%%_bDGray%lMagenta/dGray %_fBMag%%_bBRed%lMagenta/lRed %_fBMag%%_bBGreen%lMagenta/lGreen %_fBMag%%_bBYellow%lMagenta/lYellow %_fBMag%%_bBBlue%lMagenta/lBlue %_fBMag%%_bBCyan%lMagenta/lCyan %_fBMag%%_bBWhite%lMagenta/White
Echo %_RESET% Light Cyan foreground 96 (lCyan)
Echo %_fBCyan%%_bBlack% lCyan/Black %_fBCyan%%_bRed% lCyan/Red  %_fBCyan%%_bGreen% lCyan/Green  %_fBCyan%%_bYellow% lCyan/Yellow  %_fBCyan%%_bBlue% lCyan/Blue  %_fBCyan%%_bMag% lCyan/Magenta  %_fBCyan%%_bCyan% lCyan/Cyan %_fBCyan%%_bLGray% lCyan/lGray
Echo %_fBCyan%%_bDGray% lCyan/dGray %_fBCyan%%_bBRed% lCyan/lRed %_fBCyan%%_bBGreen% lCyan/lGreen %_fBCyan%%_bBYellow% lCyan/lYellow %_fBCyan%%_bBBlue% lCyan/lBlue %_fBCyan%%_bBMag% lCyan/lMagenta %_fBCyan%%_bBWhite% lCyan/White
Echo %_RESET% White foreground 97
Echo %_fBWhite%%_bBlack% White/Black %_fBWhite%%_bRed% White/Red  %_fBWhite%%_bGreen% White/Green %_fBWhite%%_bYellow% White/Yellow   %_fBWhite%%_bBlue% White/Blue  %_fBWhite%%_bMag% White/Magenta  %_fBWhite%%_bCyan% White/Cyan %_fBWhite%%_bLGray% White/lGray
Echo %_fBWhite%%_bDGray% White/dGray %_fBWhite%%_bBRed% White/lRed %_fBWhite%%_bBGreen% White/lGreen %_fBWhite%%_bBYellow% White/lYellow %_fBWhite%%_bBBlue% White/lBlue %_fBWhite%%_bBMag% White/lMagenta %_fBWhite%%_bBCyan% White/lCyan
:: reset
Echo %_RESET%
pause
:: SS64.com