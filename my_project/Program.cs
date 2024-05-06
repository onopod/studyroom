using System.Text.Json;
using (var client = new HttpClient())
{
	var response = await client.GetAsync(@"http://localhost:8000/api/users/");
	string result = await response.Content.ReadAsStringAsync();
	var json  = JsonSerializer.Deserialize<List<Prefecture>>(prefecturesJsonString);
	Console.WriteLine(json);
}
