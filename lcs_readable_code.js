let n = process.argv.length - 2
let m = new Set()
let answer = ''

function GetCommonSubstring(a, b)
{
    let res = []
    for (let i = 0; i < a.length; i++) 
    {
        for (let j = 0; j < b.length; j++) 
        {
            if (a[i] == b[j]) 
            {
                res.push(a[i])
                let i_temp = i+1
                let j_temp = j+1
                while(a[i_temp] == b[j_temp])
                {
                    if (i_temp < a.length && j_temp < b.length)
                    {
                        res[res.length-1] += a[i_temp]
                        i_temp++
                        j_temp++
                    }
                    else break
                }
            }
        }
    }
    return res
}
let strings = []
if (n > 0) for (let index = 2; index < process.argv.length; index++) strings.push(process.argv[index])    
for (let i = 0; i < strings.length; i++) 
{
    for (let j = strings.length - i - 1; j < strings.length; j++) 
    {
        if (i==j) continue
        let temps = GetCommonSubstring(strings[i], strings[j]).sort(function(arg1, arg2) { return arg2.length - arg1.length })
        for (let t = 0; t < temps.length; t++) 
        {
            let temp = temps[t]
            let check = true
            for (let k = 0; k < strings.length; k++) 
            {   
                if (!strings[k].includes(temp)) check = false
            }
            if (check)
            {
                m.add(temp)
            }
        }
        
    }
}
let p = []
for (let item of m) p.push(item)

if (p.length != 0)
{
    answer = p.sort(function(arg1, arg2) { return arg2.length - arg1.length })[0]
}
if (process.argv.length == 3) answer = process.argv[2]
console.log(answer)
