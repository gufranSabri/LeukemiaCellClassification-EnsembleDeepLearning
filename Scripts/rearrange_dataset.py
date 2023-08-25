import os
import shutil

src = r'C:\Users\gufra\Desktop\Work\Projects\AI\ALL_Classification\Datasets\Original'
all_dst = os.path.join(src, 'all')
hem_dst = os.path.join(src, 'hem')

splits = ['fold_' + str(i) for i in range(3)]

ac, hc = 0, 0
for s in splits:
    curr_path = os.path.join(src,s,s)
    classes = os.listdir(curr_path)

    for c in classes:
        print("Processing "+c)
        curr_path2 = os.path.join(curr_path,c)
        images = os.listdir(curr_path2)

        for img in images:
            if c=='all': 
                shutil.move(os.path.join(curr_path2, img), os.path.join(all_dst, img))
                ac+=1
            if c=='hem': 
                shutil.move(os.path.join(curr_path2, img), os.path.join(hem_dst, img))
                hc+=1