import seaborn as sns
import matplotlib.pyplot as plt



def boxhist(df,x):
    
    sns.set_theme(palette="Blues_r")

    # creating a figure composed of two matplotlib.Axes objects (ax_box and ax_hist)
    f, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})
 
    # assigning a graph to each ax
    ax = sns.boxplot(df[x], orient="h", ax=ax_box)
    sns.histplot(data=df, x=x, ax=ax_hist)
    
    # Remove x axis name for the boxplot
    ax.set(xlabel='')

    plt.show()


def bplts(df,x,y,w,h,xrot,orderby,lim):
    
    '''
    Function to plot bar graph for 2 variables
        df: df name
        x: x variable
        y: y variable
        w: plot width
        h: plot height
        xrot: xtick rotation (45, 30, etc.)
        orderby: display graph ('desc', 'asc')
        lim: number of x values to show (None, #)
    '''

    if orderby == 'asc':
        order = df.groupby([x])[y].mean().sort_values(ascending=True).head(lim).index
    elif orderby == 'desc':
        order = df.groupby([x])[y].mean().sort_values(ascending=False).head(lim).index
    else:
        order = None

    # setting the dimensions of the plot
    fig, ax = plt.subplots(figsize=(w, h))
    sns.barplot(df, x=x, y=y, ax=ax, errorbar=None,color='#b3cede',order=order)
    plt.title(f'{y} by {x}', fontsize=12)
    plt.ylabel(y)
    plt.xlabel(x)
    plt.xticks(rotation=xrot, ha='right')
    plt.show()



def bhplt(df,feat,w,h,wspace,bw): 
    '''
    Define function to create box plot and histograms 
        df: df name
        feat: feature name
        w: plot width
        h: plot height
        wspace: space between subplots
        bw: histogram's bin width
    '''    
    
    #Print column name
    print('Feature:', feat)  

    #Print Skew amount
    skew =  round(df[feat].skew(), 2)
    if skew > 0.5:
        print('Right Skew:',skew)
    elif skew < -0.5:
        print('Left Skew:',skew)
    else:
        print('Normal:',skew)

    # condition statement to print either median or mean
    if skew > 0.5:                          #print median
        median = df[feat].median()
        print('Median:', df[feat].median())
        line = median
    elif skew <- 0.5:
        median = df[feat].median()           #print median
        print('Median:', df[feat].median()) 
        line = median   
    else:
        mean = df[feat].mean()               #Print mean
        print('Mean:', df[feat].mean())
        line = mean

    # Set figure size
    plt.figure(figsize = (w, h))

    # Create a boxplot to visualize distribution and detect any outliers
    plt.subplot(1, 2, 1)              
    plt.title('Boxplot')
    sns.boxplot(x=df[feat],color='#b3cede')
    plt.subplots_adjust(wspace=wspace)

    # plot Histogram
    plt.subplot(1, 2, 2)   
    sns.histplot(x=df[feat],binwidth=bw,color='#b3cede', edgecolor='#78a9c8')
    plt.title('Histogram')
    plt.show()


def htplot(df,feat,w,h,bw):
    '''
    Define function to create histograms 
        df: df name
        feat: feature name
        w: plot width
        h: plot height
        bw: histogram's bin width
    '''    
    
    #Print column name
    print('Feature:', feat)  

    #Print Skew amount
    skew =  round(df[feat].skew(), 2)
    if skew > 0.5:
        print('Right Skew:',skew)
    elif skew < -0.5:
        print('Left Skew:',skew)
    else:
        print('Normal:',skew)

    # condition statement to print either median or mean
    if skew > 0.5:                          #print median
        median = df[feat].median()
        print('Median:', df[feat].median())
        line = median
    elif skew <- 0.5:
        median = df[feat].median()           #print median
        print('Median:', df[feat].median()) 
        line = median   
    else:
        mean = df[feat].mean()               #Print mean
        print('Mean:', df[feat].mean())
        line = mean

    # Set figure size
    plt.figure(figsize = (w, h))

    # plot Histogram 
    sns.histplot(x=df[feat],binwidth=bw,color='#b3cede', edgecolor='#78a9c8')
    plt.title('Histogram')
    plt.show()


def ctplt(df, x, y, w, h, lim, xrot,xaxis:str, asc, lbl:str, lbl_type:str,hue):
    '''
    Function to plot count graph
        df: df name
        x: x variable
        w: plot width
        h: plot height
        lim: number of x values to display 
        xrot: xtick rotation degree
        xaxis: keep order of xaxis (y/n)
        asc: order by ascending (True,False)
        lbl: display bar labels ('y','n')
        lbl_type: display as count or percentage ('%','#')
        hue: column to separate data colors by
    '''

    if y == None and xaxis == 'n':
        order=df[x].value_counts(ascending=asc).head(lim).index
    elif y == None and xaxis == 'y':
        order=df[x].head(lim).index
    elif x == None:
        order=df[y].value_counts(ascending=asc).head(lim).index
    else:
        None

    fig = plt.figure(figsize=(w,h))
    
    if x == None:
        ax = sns.countplot(data=df, y=y, hue=hue, order=order, palette='Blues')
    else:
        ax = sns.countplot(data=df, x=x, hue=hue, order=order, palette='Blues')
        
    plt.xticks(rotation=xrot)
    ax.tick_params(left=False, bottom=False) # Remove ticks
    sns.despine(left=True, bottom=True) # Remove borders borders

# display label to bars based on plot orientation and label type
    if y == None and lbl == 'y':
        for patch in ax.patches:
            count = patch.get_height()
            percentage = (count / len(df)) * 100
            if lbl_type == '%':
                label = f"{percentage:.1f}%"  # Format as percentage with one decimal
            elif lbl_type == '#':
                label = f"{count:.0f}"  # Format as percentage with one decimal
            else:
                label=None   
            x = patch.get_x() + patch.get_width() / 2 # Place the label at the top center of the bar
            y = patch.get_height() + 0.1  # Adjust y position for better placement
            ax.text(x, y, label, ha='center', va='bottom')
    elif x == None and lbl == 'y':
        for patch in ax.patches:
            count = patch.get_width()
            percentage = (count / len(df)) * 100
            if lbl_type == '%':
                label = f"{percentage:.1f}%"  # Format as percentage with one decimal
            elif lbl_type == '#':
                label = f"{count:.0f}"  # Format as percentage with one decimal
            else:
                label=None   
            x = patch.get_x() + patch.get_width() +.1 
            y = patch.get_y() + patch.get_height() /2 
            ax.text(x, y, label, ha='left', va='center')
    else:
        label = None