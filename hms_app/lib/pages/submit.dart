import 'package:flutter/material.dart';
import 'package:hms_app/pages/home_page.dart';

class Submission extends StatelessWidget {
  const Submission({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text(
            'HMS',
            style: TextStyle(
                color: Colors.black, fontSize: 18, fontWeight: FontWeight.bold),
          ),
          backgroundColor: Colors.white,
          elevation: 0.0,
          centerTitle: true,
        ),
        body: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const Text(
                  "Assignment Title",
                  style: TextStyle(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                      color: Colors.black),
                ),
                const SizedBox(height: 24.0),
                const Text("Assignment content will be displayed here"),
                const SizedBox(height: 24.0),
                ElevatedButton(
                  onPressed: () {
                    print("Button pressed");
                  },
                  child: const Text("Complete This Assignment"),
                ),
                const SizedBox(height: 24.0),
                const Text("Uploaded video title will display here"),
                const SizedBox(height: 24.0),
                ElevatedButton(
                  onPressed: () {
                    print("Button pressed");
                  },
                  child: const Text("Complete This Assignment"),
                ),
                const SizedBox(height: 24.0),
                ElevatedButton(
                  onPressed: () {
                    Navigator.push(context,
                        MaterialPageRoute(builder: (context) => HomePage()));
                  },
                  child: const Text("back to home"),
                ),
              ],
            )));
  }
}
