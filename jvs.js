var arr = input("Enter your numbers").split(",")

var arr1 = new Array();

for(i = 0;i<arr.length;i++)
{
	if(arr[i] != 0)
	{
		arr1.push(arr[i]);
	}
}