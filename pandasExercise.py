import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv(, encoding = "ISO-8859-1")

def read_data(path):
    column_names = ["Class", "Age", "Menopause", "Tumor_Size", "Inv_Nodes", "Node_Caps", "Deg_Malig", "Side", "location", "Irradiation"]
    df = pd.read_csv(path, encoding="ISO-8859-1", names= column_names)
    return df
def common_class(df):
    common = df['Class'].value_counts()
    print(common)
    return common

def common_age_mono(df):
    is_recurr_events = df['Class'] == 'recurrence-events'
    recurrence_events= df[is_recurr_events]
    common_age = recurrence_events['Age'].value_counts()
    common_menopause = recurrence_events['Menopause'].value_counts()
    print('Common Ages',common_age)
    print('Common Menopause', common_menopause)

def plot_recurrence_age(df):
    is_recurr_events = df['Class'] == 'recurrence-events'
    recurrence_events = df[is_recurr_events]
    common_age = recurrence_events['Age'].value_counts().sort_index()
    common_age.plot(kind='bar')
    plt.xlabel('Age')
    plt.ylabel('Number of Recurrences')
    plt.show()

df = read_data('breast-cancer.data')

common_class(df)
common_age_mono(df)
plot_recurrence_age(df)
