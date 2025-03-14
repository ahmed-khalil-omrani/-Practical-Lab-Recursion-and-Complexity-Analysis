def maxDepth(fs):
    keys=fs.keys()#tke the keys of fs
    for key in keys:#itrate all the keys
        if(fs[key]==None):
            return 0#if key have no sub dict return 0
        return maxDepth(fs[key])+1#sume of all subdict it takes only the longest path because it enter in the same layer at the same time
#O(n^x)









file_system = {
        "home": {
        "user": {
            "documents": {
                "project": {
                    "file1.txt": None,
                    "file2.txt": None

                    }                       

                }

         },
    "downloads": {
        "movie.mp4": None

        }

        }
}
print(maxDepth(file_system))
#BFS Complexity=O(n)
#the BFS is more efficent