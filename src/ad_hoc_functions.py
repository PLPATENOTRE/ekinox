from sklearn.metrics import confusion_matrix

def add_info(df, classe):
    """
    Add relevant info : mean of grades and flag if pass or not
    """
    # Compute average grade
    df['Gmean_{}'.format(classe)] = df[['G1_{}'.format(classe),'G2_{}'.format(classe)]].mean(axis=1)

    # Flag classe
    df['flag_{}'.format(classe)] = 1
    
    # Pass or Fail flag
    df['pass_{}'.format(classe)] = [0 if x < 10 else 1 for x in df['G3_{}'.format(classe)]]
    
    return df


def plot_confusion_matrix(test_y, predict_y):
    
    """
    Plot confusion matrix, precision matrix and recall matrix
    """
    
    C = confusion_matrix(test_y, predict_y)
    A =(((C.T)/(C.sum(axis=1))).T)
    B =(C/C.sum(axis=0))
    plt.figure(figsize=(30,8))
    labels = [0,1]
    
    cmap=sns.light_palette("blue")
    plt.subplot(1, 3, 1)
    sns.heatmap(C, annot=True, cmap=cmap, fmt=".3f", annot_kws={"size": 30}, xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Class')
    plt.ylabel('Original Class')
    plt.title("Confusion matrix")
    
    plt.subplot(1, 3, 2)
    sns.heatmap(B, annot=True, cmap=cmap, fmt=".3f", annot_kws={"size": 30}, xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Class')
    plt.ylabel('Original Class')
    plt.title("Precision matrix")
    
    plt.subplot(1, 3, 3)
    # representing B in heatmap format
    sns.heatmap(A, annot=True, cmap=cmap, fmt=".3f", annot_kws={"size": 30}, xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted Class')
    plt.ylabel('Original Class')
    plt.title("Recall matrix")
    
    plt.show()

