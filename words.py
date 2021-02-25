diag_report = """
Date/Time:        2021-02-15 18:35:55.126 +0530
End time:         2021-02-15 18:40:05.779 +0530
OS Version:       macOS 11.0.1 (Build 20B29)
Architecture:     x86_64h
Report Version:   32
Incident Identifier: 861FCA0F-F261-4E2E-9B15-F85A076F32BD

Data Source:      Microstackshots
Shared Cache:     9F6FFF1F-4096-355B-B037-8DCE73A7AA42 slid base address 0x7fff2002c000, slide 0x2c000

Command:          Google Chrome
Path:             /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
Identifier:       com.google.Chrome
Version:          88.0.4324.150 (4324.150)
PID:              18956

Event:            wakeups
Action taken:     none
Wakeups:          45001 wakeups over the last 251 seconds (180 wakeups per second average), exceeding limit of 150 wakeups per second over 300 seconds
Wakeups limit:    45000
Limit duration:   300s
Wakeups caused:   45001
Wakeups duration: 251s
Duration:         250.65s
Duration Sampled: 241.20s
Steps:            9

Hardware model:   MacBookPro15,4
Active cpus:      8
Boot args:        chunklist-security-epoch=0 -chunklist-no-rev2-dev

Fan speed:        0 rpm

Heaviest stack for the target process:
  6  thread_start + 15 (libsystem_pthread.dylib + 9339) [0x7fff2033547b]
  6  _pthread_start + 224 (libsystem_pthread.dylib + 26960) [0x7fff20339950]
  6  ChromeMain + 17314803 (Google Chrome Framework + 17338515) [0x10b135093]
  6  ChromeMain + 17223081 (Google Chrome Framework + 17246793) [0x10b11ea49]
  6  ChromeMain + 5143917 (Google Chrome Framework + 5167629) [0x10a599a0d]
  6  ChromeMain + 16978073 (Google Chrome Framework + 17001785) [0x10b0e2d39]
  6  ChromeMain + 17122719 (Google Chrome Framework + 17146431) [0x10b10623f]
  4  ChromeMain + 17406762 (Google Chrome Framework + 17430474) [0x10b14b7ca]
  4  ChromeMain + 17118747 (Google Chrome Framework + 17142459) [0x10b1052bb]
  3  ChromeMain + 17119384 (Google Chrome Framework + 17143096) [0x10b105538]
  3  ChromeMain + 17075097 (Google Chrome Framework + 17098809) [0x10b0fa839]
  2  ChromeMain + 17075701 (Google Chrome Framework + 17099413) [0x10b0faa95]
  2  ChromeMain + 17074424 (Google Chrome Framework + 17098136) [0x10b0fa598]
  2  ChromeMain + 17126610 (Google Chrome Framework + 17150322) [0x10b107172]
  2  ChromeMain + 17102888 (Google Chrome Framework + 17126600) [0x10b1014c8]
  1  ChromeMain + 17112233 (Google Chrome Framework + 17135945) [0x10b103949]


Powerstats for:   Google Chrome (Chrome) [18956]
UUID:             48788BA2-B782-31C9-866F-0FE85295422A
App Version:      88.0.4324.150
Build Version:    4324.150
Path:             /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
Architecture:     x86_64
Footprint:        104.77 MB -> 111.86 MB (+7268 KB)
Pageins:          556 pages
Start time:       2021-02-15 18:36:00.789 +0530
End time:         2021-02-15 18:40:01.991 +0530
Num samples:      9 (100%)
Primary state:    4 samples Frontmost App, Non-Suppressed, User mode, Effective Thread QoS Unspecified, Requested Thread QoS Unspecified, Override Thread QoS Unspecified
User Activity:    0 samples Idle, 9 samples Active
Power Source:     9 samples on Battery, 0 samples on AC
  6  thread_start + 15 (libsystem_pthread.dylib + 9339) [0x7fff2033547b]
    6  _pthread_start + 224 (libsystem_pthread.dylib + 26960) [0x7fff20339950]
      6  ChromeMain + 17314803 (Google Chrome Framework + 17338515) [0x10b135093]
        6  ChromeMain + 17223081 (Google Chrome Framework + 17246793) [0x10b11ea49]
          6  ChromeMain + 5143917 (Google Chrome Framework + 5167629) [0x10a599a0d]
            6  ChromeMain + 16978073 (Google Chrome Framework + 17001785) [0x10b0e2d39]
              6  ChromeMain + 17122719 (Google Chrome Framework + 17146431) [0x10b10623f]
                4  ChromeMain + 17406762 (Google Chrome Framework + 17430474) [0x10b14b7ca]
                  4  ChromeMain + 17118747 (Google Chrome Framework + 17142459) [0x10b1052bb]
                    3  ChromeMain + 17119384 (Google Chrome Framework + 17143096) [0x10b105538]
                      3  ChromeMain + 17075097 (Google Chrome Framework + 17098809) [0x10b0fa839]
                        2  ChromeMain + 17075701 (Google Chrome Framework + 17099413) [0x10b0faa95]
                          2  ChromeMain + 17074424 (Google Chrome Framework + 17098136) [0x10b0fa598]
                            2  ChromeMain + 17126610 (Google Chrome Framework + 17150322) [0x10b107172]
                              2  ChromeMain + 17102888 (Google Chrome Framework + 17126600) [0x10b1014c8]
                                1  ChromeMain + 17112233 (Google Chrome Framework + 17135945) [0x10b103949]
                                1  ChromeMain + 17112182 (Google Chrome Framework + 17135894) [0x10b103916]
                                  1  ChromeMain + 16962360 (Google Chrome Framework + 16986072) [0x10b0defd8]
                        1  ChromeMain + 17075822 (Google Chrome Framework + 17099534) [0x10b0fab0e]
                    1  ChromeMain + 17120273 (Google Chrome Framework + 17143985) [0x10b1058b1]
                      1  ChromeMain + 17081608 (Google Chrome Framework + 17105320) [0x10b0fc1a8]
                        1  ChromeMain + 17113973 (Google Chrome Framework + 17137685) [0x10b104015]
                2  ChromeMain + 17406880 (Google Chrome Framework + 17430592) [0x10b14b840]
                  2  kevent64 + 10 (libsystem_kernel.dylib + 40414) [0x7fff2030ddde]
                    2  <Kernel mode>
  3  start + 1 (libdyld.dylib + 87601) [0x7fff20354631]
    3  main + 285 (Google Chrome + 16109) [0x1074c1eed]
      3  ChromeMain + 264 (Google Chrome Framework + 23976) [0x10a0b1da8]
        3  ChromeMain + 16728146 (Google Chrome Framework + 16751858) [0x10b0a5cf2]
          3  ChromeMain + 16726928 (Google Chrome Framework + 16750640) [0x10b0a5830]
            3  ChromeMain + 16732195 (Google Chrome Framework + 16755907) [0x10b0a6cc3]
              3  ChromeMain + 16732921 (Google Chrome Framework + 16756633) [0x10b0a6f99]
                3  ChromeMain + 5124201 (Google Chrome Framework + 5147913) [0x10a594d09]
                  3  ChromeMain + 5142370 (Google Chrome Framework + 5166082) [0x10a599402]
                    3  ChromeMain + 5135852 (Google Chrome Framework + 5159564) [0x10a597a8c]
                      3  ChromeMain + 17979709 (Google Chrome Framework + 18003421) [0x10b1d75dd]
                        3  ChromeMain + 16978073 (Google Chrome Framework + 17001785) [0x10b0e2d39]
                          3  ChromeMain + 17122719 (Google Chrome Framework + 17146431) [0x10b10623f]
                            3  ChromeMain + 17339154 (Google Chrome Framework + 17362866) [0x10b13afb2]
                              3  ChromeMain + 17343286 (Google Chrome Framework + 17366998) [0x10b13bfd6]
                                3  -[NSApplication run] + 586 (AppKit + 195546) [0x7fff22c39bda]
                                  3  ChromeMain + 19150337 (Google Chrome Framework + 19174049) [0x10b2f52a1]
                                    3  ChromeMain + 17327866 (Google Chrome Framework + 17351578) [0x10b13839a]
                                      3  ChromeMain + 19150463 (Google Chrome Framework + 19174175) [0x10b2f531f]
                                        3  -[NSApplication(NSEvent) _nextEventMatchingEventMask:untilDate:inMode:dequeue:] + 1366 (AppKit + 251723) [0x7fff22c4774b]
                                          3  _DPSNextEvent + 883 (AppKit + 257925) [0x7fff22c48f85]
                                            3  _BlockUntilNextEventMatchingListInModeWithFilter + 64 (HIToolbox + 199407) [0x7fff2869baef]
                                              2  ReceiveNextEventCommon + 709 (HIToolbox + 200140) [0x7fff2869bdcc]
                                                2  RunCurrentEventLoopInMode + 292 (HIToolbox + 200656) [0x7fff2869bfd0]
                                                  2  CFRunLoopRunSpecific + 563 (CoreFoundation + 521918) [0x7fff2042f6be]
                                                    1  __CFRunLoopRun + 1426 (CoreFoundation + 525097) [0x7fff20430329]
                                                      1  _pthread_mutex_firstfit_lock_slow + 211 (libsystem_pthread.dylib + 8636) [0x7fff203351bc]
                                                        1  __psynch_mutexwait + 10 (libsystem_kernel.dylib + 12486) [0x7fff203070c6]
                                                          1  <Kernel mode, Effective Thread QoS User Interactive, Requested Thread QoS User Interactive>
                                                    1  __CFRunLoopRun + 890 (CoreFoundation + 524561) [0x7fff20430111]
                                                      1  __CFRunLoopDoSources0 + 248 (CoreFoundation + 530143) [0x7fff204316df]
                                                        1  __CFRunLoopDoSource0 + 180 (CoreFoundation + 530788) [0x7fff20431964]
                                                          1  __CFRUNLOOP_IS_CALLING_OUT_TO_A_SOURCE0_PERFORM_FUNCTION__ + 17 (CoreFoundation + 530940) [0x7fff204319fc]
                                                            1  ChromeMain + 17340287 (Google Chrome Framework + 17363999) [0x10b13b41f]
                                                              1  ChromeMain + 17327866 (Google Chrome Framework + 17351578) [0x10b13839a]
                                                                1  ChromeMain + 17341856 (Google Chrome Framework + 17365568) [0x10b13ba40]
                                                                  1  ChromeMain + 17118747 (Google Chrome Framework + 17142459) [0x10b1052bb]
                                                                    1  ChromeMain + 17120028 (Google Chrome Framework + 17143740) [0x10b1057bc]
                                                                      1  ChromeMain + 17060377 (Google Chrome Framework + 17084089) [0x10b0f6eb9]
                                                                        1  ChromeMain + 19460993 (Google Chrome Framework + 19484705) [0x10b341021]
                                                                          1  ChromeMain + 19369982 (Google Chrome Framework + 19393694) [0x10b32ac9e]
                                                                            1  ChromeMain + 19367738 (Google Chrome Framework + 19391450) [0x10b32a3da]
                                                                              1  ChromeMain + 19399277 (Google Chrome Framework + 19422989) [0x10b331f0d]
                                                                                1  ChromeMain + 19401286 (Google Chrome Framework + 19424998) [0x10b3326e6]
                                                                                  1  ChromeMain + 19377807 (Google Chrome Framework + 19401519) [0x10b32cb2f]
                                                                                    1  ChromeMain + 7814171 (Google Chrome Framework + 7837883) [0x10a8258bb]
                                                                                      1  ChromeMain + 7829404 (Google Chrome Framework + 7853116) [0x10a82943c]
                                                                                        1  ChromeMain + 7812033 (Google Chrome Framework + 7835745) [0x10a825061]
                                                                                          1  ChromeMain + 20274110 (Google Chrome Framework + 20297822) [0x10b40785e]
                                                                                            1  ChromeMain + 31352473 (Google Chrome Framework + 31376185) [0x10be98339]
                                                                                              1  ChromeMain + 31360141 (Google Chrome Framework + 31383853) [0x10be9a12d]
                                                                                                1  ChromeMain + 31360600 (Google Chrome Framework + 31384312) [0x10be9a2f8]
                                                                                                  1  ChromeMain + 31312688 (Google Chrome Framework + 31336400) [0x10be8e7d0]
                                                                                                    1  <Effective Thread QoS User Interactive, Requested Thread QoS User Interactive>
                                              1  ReceiveNextEventCommon + 676 (HIToolbox + 200107) [0x7fff2869bdab]
                                                1  _DropPendingBoost + 49 (HIToolbox + 308344) [0x7fff286b6478]
                                                  1  _CFRelease + 244 (CoreFoundation + 1359090) [0x7fff204fbcf2]
                                                    1  __CFMachPortBoostDeallocate + 25 (CoreFoundation + 780597) [0x7fff2046e935]
                                                      1  voucher_decrement_importance_count4CF + 83 (libdispatch.dylib + 145360) [0x7fff201ae7d0]
                                                        1  mach_voucher_attr_command + 211 (libsystem_kernel.dylib + 18972) [0x7fff20308a1c]
                                                          1  mach_msg_trap + 10 (libsystem_kernel.dylib + 3710) [0x7fff20304e7e]
                                                            1  <Kernel mode, Effective Thread QoS User Interactive, Requested Thread QoS User Interactive>

  Binary Images:
           0x1074be000 -        0x1074edfff  com.google.Chrome 88.0.4324.150 (4324.150)           <48788BA2-B782-31C9-866F-0FE85295422A>  /Applications/Google Chrome.app/Contents/MacOS/Google Chrome
           0x10a0ac000 -        0x113e0bfff  com.google.Chrome.framework 88.0.4324.150 (4324.150) <FEB7CEB5-7F0E-36EA-993B-0830056237AB>  /Applications/Google Chrome.app/Contents/Frameworks/Google Chrome Framework.framework/Versions/88.0.4324.150/Google Chrome Framework
        0x7fff2018b000 -     0x7fff201cffff  libdispatch.dylib (1271.40.12)                       <C55547DC-A05B-34A1-BD41-D54948D8F57F>  /usr/lib/system/libdispatch.dylib
        0x7fff20304000 -     0x7fff20332fff  libsystem_kernel.dylib (7195.50.7)                   <41068F5C-74E3-3C98-9256-6A18364FB5BA>  /usr/lib/system/libsystem_kernel.dylib
        0x7fff20333000 -     0x7fff2033efff  libsystem_pthread.dylib (454.40.3)                   <78072EC6-2257-361A-AAF5-4A3C1832B5EB>  /usr/lib/system/libsystem_pthread.dylib
        0x7fff2033f000 -     0x7fff20379fff  libdyld.dylib (832.7.1)                              <0C66AB9F-E22C-3286-B76B-DA4008698CD2>  /usr/lib/system/libdyld.dylib
        0x7fff203b0000 -     0x7fff2084bfff  com.apple.CoreFoundation 6.9 (1770.106)              <7EBD4941-5978-33EF-98FB-724BB81E92C8>  /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
        0x7fff22c0a000 -     0x7fff23966fff  com.apple.AppKit 6.9 (2022.10.104)                   <FA93F8CC-AB69-3E81-AC53-3FA08704738C>  /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
        0x7fff2866b000 -     0x7fff2896afff  com.apple.HIToolbox 2.1.1 (1060.0.1)                 <97A715C9-6C47-388D-8801-A44FB84E5C4D>  /System/Library/Frameworks/Carbon.framework/Versions/A/Frameworks/HIToolbox.framework/Versions/A/HIToolbox
"""
