import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_preprocess_data():
    dataset_url = "https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt"
    columns = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes',
               'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
               'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
               'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
               'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
               'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
               'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
               'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
               'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
               'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label']

    df = pd.read_csv(dataset_url, names=columns)

    # Encode categorical features
    categorical_columns = ['protocol_type', 'service', 'flag', 'label']
    for col in categorical_columns:
        df[col] = LabelEncoder().fit_transform(df[col])

    # Feature-target split
    X = df.drop(columns=['label'])
    y = df['label']

    # Data normalization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
:wq


