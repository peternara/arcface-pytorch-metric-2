class Config(object):
    env = "default"
    backbone = "resnet18"
    classify = "softmax"
    num_classes = 10575
    metric = "arc_margin"

    train_root = "data/Datasets/lfw/lfw-align-128/" #"data/Datasets/CASIA-WebFace/CASIA-WebFace/"
    train_list = "data/Datasets/lfw/train_data.txt" #"data/Datasets/CASIA-WebFace/train_data.txt"
    val_list = "data/Datasets/lfw/valid_data.txt" #"data/Datasets/CASIA-WebFace/valid_data.txt"

    test_root = "data1/Datasets/anti-spoofing/test/data_align_256"
    test_list = "test.txt"

    checkpoints_path = "checkpoints"
    load_model_path = "models/resnet18.pth"
    test_model_path = "checkpoints/resnet18_30.pth"
    train_model_path = "checkpoints/resnet18_30.pth"
    save_interval = 10

    train_batch_size = 50  # batch size
    test_batch_size = 60

    input_shape = (1, 128, 128)

    optimizer = "sgd"

    use_gpu = False  # use GPU or not
    gpu_id = "0"
    num_workers = 4  # how many workers for loading data
    print_freq = 100  # print info every N batch

    debug_file = "/tmp/debug"  # if os.path.exists(debug_file): enter ipdb
    result_file = "result.csv"

    max_epoch = 50
    lr = 1e-1  # initial learning rate
    lr_step = 10
    lr_decay = 0.95  # when val_loss increase, lr = lr*lr_decay
    weight_decay = 5e-4
