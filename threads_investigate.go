package main

import (
	"fmt"
	"sync"
	"time"
)

var startTime time.Time

func incrementCounter(wg *sync.WaitGroup) {
	defer wg.Done()
	counter := 0

	for i := 0; i < 1000000; i++ {
		counter++
	}

	finishedTimeThread := time.Since(startTime).Seconds()
	fmt.Printf("Time %.2f seconds - Goroutine finished! Counter value - %d\n", finishedTimeThread, counter)
}

func runThreads() {
	var wg sync.WaitGroup
	startTime = time.Now()

	wg.Add(1)
	go incrementCounter(&wg)
	wg.Add(1)
	go incrementCounter(&wg)

	wg.Wait()

	endTime := time.Since(startTime).Seconds()
	fmt.Printf("Execution time: %.4f seconds\n", endTime)
}

func main() {
	runThreads()
}
