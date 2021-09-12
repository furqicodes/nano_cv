Conda version: 4.7.1
Python version: 3.5
Dataset image size: 640x480 px

"""
Also, find the train_input_reader and eval_input_reader tags and change the input path. The path should point to the train.record and test.record files you created. Moreover, label_map_path should point to the location of the label map.
train_input_reader: {
 tf_record_input_reader {
  input_path: “./train.record”
 }
 label_map_path: “./labelmap.pbtxt”
}
eval_input_reader: {
 tf_record_input_reader {
  input_path: “./test.record”
 }
 label_map_path: “./labelmap.pbtxt”
 shuffle: false
 num_readers: 1
}
"""
