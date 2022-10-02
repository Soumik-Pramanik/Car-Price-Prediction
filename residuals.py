data['log price'] = np.log(data['price'])
model_1_results = pd.DataFrame({'log price fitted': model_1_pred, 'residuals': model_1_fit.resid})
with plt.rc_context(rc = {'figure.dpi': 500, 'axes.labelsize': 10, 
                          'xtick.labelsize': 9, 'ytick.labelsize': 9}): 

    fig_3, ax_3 = plt.subplots(3, 3, figsize = (10.5, 9))
    ax_flat = ax_3.flatten()
    
    ### Plots № 1 - 3
    
    sns.scatterplot(ax = ax_flat[0], y = model_1_results['residuals'], x = data['horsepower'], 
                    s = 9.5, color = 'k')
    
    ax_flat[0].set_title('a) Residuals vs $X_5$', fontsize = 11, color = 'black')
    ax_flat[0].axvspan(xmin = 250, xmax = 300, 
                       ymin = 0.02, ymax = 0.27, 
                       alpha = 0.2, color = 'red')
    
    sns.scatterplot(ax = ax_flat[1], y = model_1_results['residuals'], x = data['wheelbase'],
                    s = 9.5, color = 'k')
    
    ax_flat[1].set_title('b) Residuals vs $X_6$', fontsize = 11, color = 'black')

    sns.scatterplot(ax = ax_flat[2], y = model_1_results['residuals'], 
                    x = model_1_results['log price fitted'], s = 9.5, color = 'k')
    
    ax_flat[2].set_title('c) Residuals vs $\hatY$', fontsize = 11, color = 'black')
    ax_flat[2].axvspan(xmin = 10.5, xmax = 11, 
                       ymin = 0.02, ymax = 0.27, 
                       alpha = 0.2, color = 'red')
    
    ### Plots № 3 - 6
    
    sns.scatterplot(ax = ax_flat[3], y = model_1_results['residuals'], x = Y.index,
                    s = 9.5, color = 'k')
    
    ax_flat[3].set_title('d) Residual scatterplot', fontsize = 11, color = 'black')
    
    sns.histplot(ax = ax_flat[4], x = model_1_results['residuals'], kde = True,
                 color = 'k')
    
    ax_flat[4].set_title('e) Residual histogram', fontsize = 11, color = 'black')
    
    sm.qqplot(model_1_results['residuals'], line = 'q', markerfacecolor = 'k', 
              markeredgecolor = 'k', markersize = 2, ax = ax_flat[5])
    
    ax_flat[5].set_title('f) Residual qq-plot', fontsize = 11, color = 'black')
    
    ### Plot № 7
    
    sns.scatterplot(ax = ax_flat[6], y = model_1_results['residuals'], x = data['log price'],
                    s = 9.5, color = 'k')
    
    ax_flat[6].set_title('g) Residuals vs $Y$', fontsize = 11, color = 'black')
    x_1 = np.linspace(8.5, 10.5, 100)
    ax_flat[6].plot(x_1, -0.01*(x_1/2)**2 - 0.2, color = 'r', linestyle = '--')
    ax_flat[6].plot(x_1, +0.05*(x_1/2)**2 - 0.75, color = 'r', linestyle = '--')
    
    [axes.set_visible(False) for axes in ax_flat[7:]]
    
    #fig_3.suptitle('Residual analysis', fontsize = 30)
    plt.tight_layout(pad = 1)
    plt.show()
    
