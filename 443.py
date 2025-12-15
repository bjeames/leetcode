class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            start = read

            while read < n and chars[start] == chars[read]:
                read += 1

            chars[write] = chars[start]
            write +=1

            count = read - start
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
        
        return write


            


