#! /opt/rh/python27/root/usr/bin/python

""" AUTHOR and PREAMBLE (AIM)
NADEAU--150218
AIM: (!!! Example only !!! Does not correspond to this program !!!)
  = YD slice
    . Read in data file (having xyz coords.)
    . Extract data for fixed Y coord
    . make subsets across D steps
    . output to file as (Y D coord) (original line)
    . Next fixed Y and repeat
    . coninue until binning of entire surface complete
    . Save to file
"""


""" VERSION
Version Python 2.7.5 of python is:
#! /opt/rh/python27/root/usr/bin/python

Version Redhat 6 2.6.6 of python is:
#! /usr/bin/python

# To find default version for a computer
# simply use:
# [ python 
# on the command line
"""

""" CALL E.G.:
   (SEE: /data/hrsn1/hfn6/aurelie/TRMR_MONIT/RM.proc
      section on: Stacking w/ perentile(s) )
   [ cd /data/hrsn1/hfn6/aurelie/TRMR_MONIT/POST-M6.050114/2015/047
     set utl = /data/hrsn1/hfn6/aurelie/TRMR_MONIT/UTL
     set cSET = "BP.Bf1"
     set cSET = "BP.Bf23"
     set cSET = "PB.Bf12"
     set cSET = "PB.BfZ"
     set cSET = "BP.Bf123_PB.BfZ12"
     set cSET = "BK.BfZNE"
     set cSET = "BP.Bf123_PB.BfZ12_BK.BfZNE"
     set if = lll
     $utl/mrow-sort.py $if |egrep -v 'None' > look_"$cSET"
     ~/S_bin/mbells
     ]]]
"""

""" IMPORTS """
import sys
import math
import subprocess
import numpy as np
import pandas as pd
from pandas import Series, DataFrame


""" COMMAND-LINE ARGUMENTS """
#print >>sys.stderr
#print >>sys.stderr, 'Number of arguments:', len(sys.argv), 'arguments.'
#print >>sys.stderr
#for i in range(0,len(sys.argv)):
#    print >>sys.stderr, "argv",i,"is: ", sys.argv[i]

""" ASSIGN ARGUMENTS TO VARIABLES"""
prog=str(sys.argv[0])
FN=str(sys.argv[1])

#params=['prog','FN','strtY','endY','strtD','endD','binW','hlfW','stp']
#params=['prog','FN']
#for i in range(0,(len(sys.argv)) ):
#    print >>sys.stderr, "%+10s:  %+5s"%( params[i],eval(params[i]) )


""" READ DATA FILE into DATAFRAME (df) """
## ALL rows:
#df=pd.read_table(FN,sep='\s+',header=None,dtype='str')
## Only first nrows:
#df=pd.read_table(FN,sep='\s+',nrows=100,header=None,dtype='str')
#df=pd.read_table(FN,sep='\s+',nrows=1000,header=None,dtype='str')
df=pd.read_table(FN,sep='\s+',           header=None,dtype='str')
df=df.astype('float128')


""" View/Evaluate shape/dimensions/column_types """
#print  >>sys.stderr
#print   >>sys.stderr,"---------"
#print   >>sys.stderr,"# Number of rows and columns in df "
#print   >>sys.stderr,df.shape  
#print   >>sys.stderr,"# Number of rows df "
#print   >>sys.stderr,len(df)
#print   >>sys.stderr,"# Name of columns in df "
#print   >>sys.stderr,df.columns
#print   >>sys.stderr,"# Obtain dtypes for every column"
#print   >>sys.stderr,df.dtypes
#print type(df)
#print df


""" Select and View by Rows and Columns """
#rowT=df.T
#print df[10:11]
#rowT=df[10:11].T
#print rowT
#print rowT.sort_index(by=10)
#print rowT.sort_index(by=10).reset_index(drop=True)
#print rowT.sort_index(by=10).reset_index(drop=True).T

### LOOP
rS=rI=00+0
rE=len(df)+0
#print rS,rI,rE
while rI <= rE:
    rowT=df[rI:rI+1].T
    print rowT.sort_index(by=rI).reset_index(drop=True).T.to_csv(sys.stdout,sep=' ',dtype='float', index=False, header=False)
    rI=rI+1


sys.exit()


"""  STUFF BELOW """
"""  STUFF BELOW """
"""  STUFF BELOW """

""" CONVERT DTYPES """
print  >>sys.stderr,"# Convert dtype of all columns in DataFrame from object-->numeric"
print  >>sys.stderr, "#   when possible.  BAD part is it truncates the Ydec data in column 4"
print  >>sys.stderr, "#   because is is out to so many decimal place"
#df=df.convert_objects(convert_numeric=True)
#print df
#print df.dtypes

print >>sys.stderr, "# Convert dtype of select columns to select dtypes (e.g., object-->numeric) #"
print >>sys.stderr, "# Convert dtype of select columns to select dtypes "
print >>sys.stderr, "#   (e.g., object-->numeric) "
print >>sys.stderr, "## Specific dtypes"
#df=pd.read_table(FN,sep='\s+',nrows=7,header=None,dtype='str')
#df[0]=df[0].astype('float128')
#df[1]=df[1].astype('float128')
#df[2]=df[2].astype('float128')
#df[5]=df[5].astype('float128')
#df[6]=df[6].astype('float128')
#df[7]=df[7].astype('float128')
#df[8]=df[8].astype('float128')
#df[9]=df[9].astype('float128')
#print df
#print df.dtypes

print >>sys.stderr, "## Or convert_numeric defaults dtypes"
#df=pd.read_table(FN,sep='\s+',nrows=7,header=None,dtype='str')
#df[0]=df[0].convert_objects(convert_numeric=True)
#df[1]=df[1].convert_objects(convert_numeric=True)
#df[2]=df[2].convert_objects(convert_numeric=True)
#df[5]=df[5].convert_objects(convert_numeric=True)
#df[6]=df[6].convert_objects(convert_numeric=True)
#df[7]=df[7].convert_objects(convert_numeric=True)
#df[8]=df[8].convert_objects(convert_numeric=True)
#df[9]=df[9].convert_objects(convert_numeric=True)
#print df
#print df.dtypes

""" SORTING """
print >>sys.stderr, " ## Sorting ... ##"
#df=pd.read_table(FN,sep='\s+',nrows=10,header=None,dtype='str')
#df[0]=df[0].astype('float128')
#df[1]=df[1].astype('float128')
#df[2]=df[2].astype('float128')
#df[5]=df[5].astype('float128')
#df[6]=df[6].astype('float128')
#df[7]=df[7].astype('float128')
#df[8]=df[8].astype('float128')
#df[9]=df[9].astype('float128')
#print df.sort_index(by=1)
#print df.dtypes

""" E===EXAMPLES EXAMPLES EXAMPLES """
""" E===EXAMPLES EXAMPLES EXAMPLES """
""" E===EXAMPLES EXAMPLES EXAMPLES """



""" MAIN MAIN MAIN """
""" MAIN MAIN MAIN """
""" MAIN MAIN MAIN """

""" READ IN DATA """
print >>sys.stderr, "## Set up ##"
df=pd.read_table(FN,sep='\s+',         header=None,dtype='str')
#df=pd.read_table(FN,sep='\s+',nrows=20,header=None,dtype='str')
df[0]=df[0].astype('float128')
df[1]=df[1].astype('float128')
df[2]=df[2].astype('float128')
df[4]=df[4].astype('string')
df[5]=df[5].astype('float128')
df[6]=df[6].astype('float128')
df[7]=df[7].astype('float128')
df[8]=df[8].astype('float128')
df[9]=df[9].astype('int64')
print >>sys.stderr, df
print >>sys.stderr, df.dtypes

print >>sys.stderr, "# Extract a single value from [row,col] of DataFrame #"
#row=1
#col=1
#print df.ix[row,col]

# HHH 2
# Create first line of output dataframe with same number of columns 
# as existing df
ncol=df.shape[1]
colindx = range(0,ncol)
rowindx = [0]
#dfOUT=DataFrame(columns=[0,1],index=[0])
dfOUT=DataFrame(columns=colindx,index=rowindx)
print dfOUT


##  LOOP
# Starting at smallest Y and D coords. then
# Outer loop steps through Y 
# Inner loop steps through all D  for each Y.
#   . strtY --  Starting Y coord.
#   . strtD --  Starting D coord.
#   . binYstrt, binDstrt -- Center of first bin
#   . binYend, binDend -- Center of last bin
#   . binVy, binVd -- Values of center of individual bins 
#                     as they are cycle through. 
print >>sys.stderr, "# Select by Ranges in Y and D #"
binYstrt=float(strtY+hlfW)
binDstrt=float(strtD+hlfW)
binYend=float(endY-hlfW)
binDend=float(endD-hlfW)
binVy=binYstrt
binVd=binDstrt
print >>sys.stderr, binYstrt,binYend,binDstrt,binDend

# Loop over Y bins (binVy)
while binVy <= binYend:
    mnY=binVy-hlfW
    mxY=binVy+hlfW

    # Loop over D bins (binVd)
    while binVd <= binDend:
        mnD=binVd-hlfW
        mxD=binVd+hlfW
#       print "%06.3f"%binVy, "%06.3f"%binVd
        dfBIN=df[ ( (mnY < df[1]) & (df[1]<= mxY) ) &\
                  ( (mnD < df[2]) & (df[2] <= mxD) ) ]
        if dfBIN.empty:
            print "%06.3f %06.3f"%(binVy,binVd),"00.0000 00.0000 00.000 "\
"0000.000.000000.0000 0000.000000000000000000 00.00000 0000.00000 00.000 00.00 00000000"

          # Insert coords. of bin center
        dfBIN.insert(0,0,"%06.3f"%binVd,allow_duplicates=True)
        dfBIN.columns = range(0,len(dfBIN.columns))
        dfBIN.insert(0,0,"%06.3f"%binVy,allow_duplicates=True)
        dfBIN.columns = range(0,len(dfBIN.columns))
          # Output data for bin to:  stdout
#HHH
#       dfBIN[11]=map(lambda x: long(x), dfBIN[11]) #works
#       dfBIN[11]=map(lambda x: float(x), dfBIN[11]) #works
#       dfBIN[11]=map(lambda x: "%-9s"%(x), dfBIN[11]) #works

#       dfBIN[2]=map(lambda x: "%07.4f"%(x), dfBIN[2]) #works
#       dfBIN[3]=map(lambda x: "%07.4f"%(x), dfBIN[3]) #works
#       dfBIN[4]=map(lambda x: "%06.3f"%(x), dfBIN[4]) #works
#       dfBIN[7]=map(lambda x: "%.5f"%(x), dfBIN[7]) #works
#       dfBIN[8]=map(lambda x: "%.5f"%(x), dfBIN[8]) #works
#       dfBIN[9]=map(lambda x: "%06.3f"%(x), dfBIN[9]) #works
#       dfBIN[10]=map(lambda x: "%05.2f"%(x), dfBIN[10]) #works

# Working on this 150313
#       dfOUT.append(dfBIN,ignore_index=True)

        dfBIN.to_csv(sys.stdout,sep=' ',dtype='str',index=False, header=False)

#hhh    

#       print dfBIN
#       print dfBIN.dtypes
#       print len(dfBIN.columns)
          # Next D bin
        binVd=binVd+stp

    # Next Y bin
    binVd=binDstrt
    binVy=binVy+stp


sys.exit()
dfBIN=df[ ( (mnY < df[1]) & (df[1]< mxY) ) &\
          ( (mnD < df[2]) & (df[2] < mxD) ) ]
#dfBIN.to_csv(sys.stdout,sep=' ',dtype='str',index=False, header=False)

print "# Insert Y and D values into DataFrame #"
midY='%06.3f'%((mxY+mnY)/2.)
midD='%06.3f'%((mxD+mnD)/2.)
dfBIN.insert(0,0,midD,allow_duplicates=True)
dfBIN.columns = range(0,len(dfBIN.columns))
dfBIN.insert(0,0,midY,allow_duplicates=True)
dfBIN.columns = range(0,len(dfBIN.columns))

#print dfBIN.columns
#print len(dfBIN.columns)
#print range(0,len(dfBIN.columns))
dfBIN.columns = range(0,len(dfBIN.columns))
#print dfBIN
#print dfBIN.dtypes

#dfBIN.insert(0,0,midY,allow_duplicates=True)
dfBIN.to_csv(sys.stdout,sep=' ',dtype='str',index=False, header=False)

print
print "# Select by Range in T == long Ydec #"
#print df
#   # BEST
##mnT ='%23.18f' % 1984.047249871293843171
##mxT ='%23.18f' % 1984.080787145188196519
#   # CLOSE ENOUGH (generally)
#mnT ='%23.18f' % 1984.040
#mxT ='%23.18f' % 1984.080
#print type(mnT)
#print type(mxT)
#print mnT
#print mxT
#print df.dtypes
#print df[ (mnT < df[4]) & (df[4]< mxT) ]


#print series
#series[1].apply(str)
##print series.sum()
#print series
#print type(series)

  # tests
#df[4]=16.5
#print df

  # tests on appending/concatinating
#val=df[9]
#val2=df[4]+" "+val
#print val2

sys.exit()


""" OUTPUT DATA """
#df.to_csv(sys.stdout,sep=' ',dtype='str')
#df.to_csv(sys.stdout,sep=' ',dtype='str', index=False, header=False)


""" Extract data for fixed Y coord """
#print df[1]
#print df.ix[[1],:]
print
print df[1],df[2],df[3],df[4]
print
print

sys.exit()
print len(df)
print type(len(df))

i=0+0
print type(i)
while i < len(df):
    df.ix[[i],:].to_csv(sys.stdout,sep=' ',header=False,index=False)
    Y=float(df.ix[[i],1])
    if Y == 13.3195:
        print df.ix[[i],1]
    
    i=i+1

sys.exit()



#i=0+0
#while 1:
#    print df[i]
#    i=i+1
#

#
#    if not lll:
#        break
#
#
#    splt=lll.split()
#    X=float(splt[0])
#    Y=float(splt[1])
#    D=float(splt[2])
#    if(mnX <= X and X <= mxX):
#        if(mnY <= Y and Y <= mxY):
#          if(mnD <= D and D <= mxD):
#            otpt.write(lll)
#            sys.stdout.write(lll)
#
#sys.exit()
#
#""" Select xyd Subset and output to file"""
##otpt=open(fout,'w')
#while 1:
#    lll=process.stdout.readline()
#    if not lll:
#        break
#    splt=lll.split()
#    X=float(splt[0])
#    Y=float(splt[1])
#    D=float(splt[2])
#    if(mnX <= X and X <= mxX):
#        if(mnY <= Y and Y <= mxY):
#          if(mnD <= D and D <= mxD):
#            otpt.write(lll)
#            sys.stdout.write(lll)
#
#otpt.close()
#
##T=numpy.float64(list[4])
##    T=float(splt[4])
##print type(T), "{0:23.18f}".format(T)
#    
#
#sys.exit()
