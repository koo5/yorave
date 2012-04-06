;--------------------------------
;Include Modern UI

  !include "MUI2.nsh"

;--------------------------------
;General

  ;Name and file
  Name "Marave"
  OutFile "Marave-0.7.win32.exe"

  ;Default installation folder
  InstallDir "$LOCALAPPDATA\Marave"
  
  ;Get installation folder from registry if available
  InstallDirRegKey HKCU "Software\Marave" ""

  ;Request application privileges for Windows Vista
  RequestExecutionLevel user

;--------------------------------
;Interface Settings

  !define MUI_ABORTWARNING

;--------------------------------
;Pages

  !insertmacro MUI_PAGE_LICENSE "LICENSE"
  !insertmacro MUI_PAGE_DIRECTORY
  !insertmacro MUI_PAGE_INSTFILES
  
  !insertmacro MUI_UNPAGE_CONFIRM
  !insertmacro MUI_UNPAGE_INSTFILES
  
;--------------------------------
;Languages
 
  !insertmacro MUI_LANGUAGE "English"

;--------------------------------
;Installer Sections

Section "Install"

  SetOutPath "$INSTDIR"
  File /r "dist\marave"

  ExecWait '"$INSTDIR\vc_redist.exe" /qn /c:"VCREDI~1.EXE /q:a /c:""msiexec /i vcredist.msi /qb!"" "'
  ;Store installation folder
  WriteRegStr HKCU "Software\Marave" "" $INSTDIR
  
  ;Create uninstaller
  WriteUninstaller "$INSTDIR\Uninstall.exe"

  ;Create shortcuts
  CreateDirectory $SMPROGRAMS\Marave
  CreateShortCut "$SMPROGRAMS\Marave\Marave.lnk" "$INSTDIR\marave\marave.exe" ; use defaults for parameters, icon, etc.
  CreateShortCut "$SMPROGRAMS\Marave\Uninstall Marave.lnk" "$INSTDIR\Uninstall.exe" ; use defaults for parameters, icon, etc.

  
SectionEnd


;--------------------------------
;Uninstaller Section

Section "Uninstall"

  Delete "$INSTDIR\Uninstall.exe"
  RMDir /r "$INSTDIR"

  DeleteRegKey /ifempty HKCU "Software\Marave"

SectionEnd
